import os
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
import carcass
import hide_script
import recovery_script
import RSA_encoder
import RSA_decryptor
import pretty_errors
import time


class AppCore(QtWidgets.QMainWindow, carcass.UiApplication):
    def __init__(self):
        super(AppCore, self).__init__()
        self.ui = carcass.UiApplication()
        self.ui.setupUi(self)

        self.ui.close_button.clicked.connect(lambda: self.close_window())
        self.ui.minimize_button.clicked.connect(lambda: self.minimize_window())

        self.oldPos = self.pos()

        # buttons of clear line
        self.ui.hide_clear_path.clicked.connect(lambda: self.clear_hide_path_to_container())
        self.ui.hide_clear_save_of_file.clicked.connect(lambda: self.clear_hide_save_of_file())
        self.ui.hide_clear_text.clicked.connect(lambda: self.clear_hide_text())
        self.ui.recovery_clear_path.clicked.connect(lambda: self.clear_recovery_path_to_container())
        self.ui.recovery_clear_extraction_key.clicked.connect(lambda: self.clear_recovery_extraction_key())
        self.ui.recovery_clear_RSA_key.clicked.connect(lambda: self.clear_recovery_rsa_key())
        self.ui.recovery_clean_save_of_file.clicked.connect(lambda: self.clear_recovery_save_of_file())

        # buttons of file-dialog
        self.ui.hide_open_container.clicked.connect(lambda: self.hide_open_container())
        self.ui.hide_save_of_file_button.clicked.connect(lambda: self.hide_save_of_container())
        self.ui.recovery_open_container.clicked.connect(lambda: self.recovery_open_container())
        self.ui.recovery_open_file.clicked.connect(lambda: self.recovery_save_of_container())

        # buttons of run script
        self.ui.hide_button.clicked.connect(lambda: self.start_hide())
        self.ui.recovery_Button.clicked.connect(lambda: self.start_recovery())

    def start_hide(self):
        path = self.ui.hide_path_to_container.text()
        save_path = self.ui.hide_save_of_file.text()
        message = self.ui.hide_text.toPlainText()

        encrypt_rsa_text, rsa_key = RSA_encoder.RSA(message)
        extraction_key = hide_script.hide('%s' % path, '%s' % encrypt_rsa_text, '%s' % save_path)

        self.ui.hide_extraction_key.setText(str(extraction_key))
        self.ui.hide_RSA_key.setText(str(rsa_key))

        self.ui.hide_path_to_container.clear()
        self.ui.hide_text.clear()

    def start_recovery(self):
        path = self.ui.recovery_path_to_container.text()
        extraction_key = self.ui.recovery_extraction_key.text()
        rsa_key = self.ui.recovery_RSA_key.text()
        save_path = self.ui.recovery_save_of_file.text()

        recovery_text = recovery_script.decode(path, extraction_key)

        finish = RSA_decryptor.decryption(str(rsa_key), str(recovery_text), str(save_path))

        self.ui.notification.setText(str(finish))

        self.ui.recovery_path_to_container.clear()
        self.ui.recovery_extraction_key.clear()
        self.ui.recovery_RSA_key.clear()

    def hide_open_container(self):
        options = QtWidgets.QFileDialog.Options()
        # options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Find container", "", "Image Files(*.png *.jpg)",
                                                             options=options)
        if file_path:
            print(file_path)
            self.ui.hide_path_to_container.setText(file_path)

    def hide_save_of_container(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "", "Image Files(*.png)",
                                                             options=options)
        if file_path:
            if '.png' in file_path:
                self.ui.hide_save_of_file.setText(file_path)
            else:
                file_path = file_path + '.png'
                self.ui.hide_save_of_file.setText(file_path)

    def recovery_open_container(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Find container", "", "Image Files(*.png *.jpg)",
                                                             options=options)
        if file_path:
            self.ui.recovery_path_to_container.setText(file_path)

    def recovery_save_of_container(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "", "Text Files(*.txt)",
                                                             options=options)
        if file_path:
            if ".txt" in file_path:
                self.ui.recovery_save_of_file.setText(file_path)
            else:
                file_path = file_path + ".txt"
                self.ui.recovery_save_of_file.setText(file_path)

    def clear_hide_path_to_container(self):
        self.ui.hide_path_to_container.clear()

    def clear_hide_save_of_file(self):
        self.ui.hide_save_of_file.clear()

    def clear_hide_text(self):
        self.ui.hide_text.clear()

    def clear_recovery_path_to_container(self):
        self.ui.recovery_path_to_container.clear()

    def clear_recovery_extraction_key(self):
        self.ui.recovery_extraction_key.clear()

    def clear_recovery_rsa_key(self):
        self.ui.recovery_RSA_key.clear()

    def clear_recovery_save_of_file(self):
        self.ui.recovery_save_of_file.clear()

    def close_window(self):
        self.close()

    def minimize_window(self):
        self.showMinimized()

    def mousePressEvent(self, event):  # functions for move window
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):  # -//-
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = AppCore()
    application.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
