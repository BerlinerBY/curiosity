import os
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal
import carcass
import hide_script
import recovery_script
import RSA_decryptor
import RSA_encoder
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
        # self.ui.hide_button.clicked.connect(lambda: self.start_hide())
        # self.ui.recovery_Button.clicked.connect(lambda: self.start_recovery())
        self.ui.hide_button.clicked.connect(lambda: self.hide_button())
        self.ui.recovery_Button.clicked.connect(lambda: self.recovery_button())

    def hide_button(self):
        self.hide_worker = hide_script.HideScript(self.ui.hide_path_to_container.text(),
                                                  self.ui.hide_save_of_file.text(),
                                                  self.ui.hide_text.toPlainText())
        self.hide_worker.count_percent.connect(self.on_hide_count_percent)
        self.hide_worker.global_extraction_key.connect(self.print_extraction_key)
        self.hide_worker.global_rsa_key.connect(self.print_rsa_key)
        self.hide_worker.start()

        self.ui.hide_path_to_container.clear()
        self.ui.hide_text.clear()

    def on_hide_count_percent(self, value):
        self.ui.hide_progress.setValue(value)

    def print_extraction_key(self, value):
        self.ui.hide_extraction_key.setText(value)

    def print_rsa_key(self, value):
        self.ui.hide_RSA_key.setText(value)

    def recovery_button(self):
        self.recovery_worker = recovery_script.RecoveryScript(self.ui.recovery_path_to_container.text(),
                                                              self.ui.recovery_extraction_key.text(),
                                                              self.ui.recovery_RSA_key.text(),
                                                              self.ui.recovery_save_of_file.text())

        self.recovery_worker.count_percent.connect(self.on_recovery_count_percent)
        self.recovery_worker.global_finish.connect(self.print_finish)
        self.recovery_worker.start()

        self.ui.recovery_path_to_container.clear()
        self.ui.recovery_extraction_key.clear()
        self.ui.recovery_RSA_key.clear()

    def on_recovery_count_percent(self, value):
        self.ui.recovery_progress.setValue(value)

    def print_finish(self, value):
        self.ui.notification.setText(value)

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
