import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import main_menu
import encrypt_window
import decryption_window
import try_2
import decode_try_2
import RSA_encoder
import RSA_decryptor
import pretty_errors
import time


class Encrypt_window(QtWidgets.QMainWindow, encrypt_window.Ui_Curiosity_chipher):
    def __init__(self):
        super(Encrypt_window, self).__init__()
        self.ui = encrypt_window.Ui_Curiosity_chipher()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon('wheel.png'))

        self.ui.clear_line_adress.clicked.connect(lambda: self.clear_line_adress())
        self.ui.clear_input_text.clicked.connect(lambda: self.clear_line_text())
        self.ui.clear_save_line_adress.clicked.connect(lambda: self.clear_save_line_adress())
        self.ui.encrypt_button.clicked.connect(lambda: self.run_encrypt_script())

    def clear_line_adress(self):
        self.ui.input_adress_file.clear()

    def clear_line_text(self):
        self.ui.input_text.clear()

    def clear_save_line_adress(self):
        self.ui.input_save_adress_file.clear()

    def run_encrypt_script(self):
        adress = self.ui.input_adress_file.text()
        print("1, time: ", time.time())
        text = self.ui.input_text.toPlainText()
        print("2, time: ", time.time())
        save_adress = self.ui.input_save_adress_file.text()
        print("3, time: ", time.time())
        encrypt_rsa_text, rsa_key = RSA_encoder.RSA(text)
        print("4, time: ", time.time())
        output_your_key = try_2.encrypt('%s' % (adress), '%s' % (encrypt_rsa_text), '%s' % (save_adress))
        print("5, time: ", time.time())
        self.ui.output_decryption_key.setText(str(output_your_key))
        self.ui.output_RSA_key.setText(str(rsa_key))

        self.ui.input_adress_file.clear()
        self.ui.input_text.clear()
        self.ui.input_save_adress_file.clear()


class Decryption_Window(QtWidgets.QMainWindow, decryption_window.Ui_Curiosity_decryption):
    def __init__(self):
        super(Decryption_Window, self).__init__()
        self.ui = decryption_window.Ui_Curiosity_decryption()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('wheel.png'))

        self.ui.clear_line_adress_Button.clicked.connect(lambda: self.clear_line_adress())
        self.ui.clear_line_decryption_key_Button.clicked.connect(lambda: self.clear_decryption_key_line())
        self.ui.clear_line_RSA_key_Button.clicked.connect(lambda: self.clear_RSA_key_line())
        self.ui.clear_line_save_adress_Button.clicked.connect(lambda: self.clear_line_save_adress())

        self.ui.decryption_Button.clicked.connect(lambda: self.run_decryption())

    def clear_line_adress(self):
        self.ui.input_line_adress.clear()

    def clear_decryption_key_line(self):
        self.ui.input_line_decryption_key.clear()

    def clear_RSA_key_line(self):
        self.ui.input_line_RSA_key.clear()

    def clear_line_save_adress(self):
        self.ui.input_line_save_adress.clear()

    def run_decryption(self):
        adress = self.ui.input_line_adress.text()
        decryption_key = self.ui.input_line_decryption_key.text()
        rsa_key = self.ui.input_line_RSA_key.text()
        save_adress = self.ui.input_line_save_adress.text()

        decryption_text = decode_try_2.decode(adress, decryption_key)

        end = RSA_decryptor.decryption(str(rsa_key), str(decryption_text), str(save_adress))

        self.ui.ending.setText(str(end))

        self.ui.input_line_adress.clear()
        self.ui.input_line_decryption_key.clear()
        self.ui.input_line_RSA_key.clear()
        self.ui.input_line_save_adress.clear()


class Start_window(QtWidgets.QMainWindow, main_menu.Ui_MainWindow):
    def __init__(self):
        super(Start_window, self).__init__()
        self.ui = main_menu.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('wheel.png'))

        self.encrypt = None
        self.ui.encrypt_button.clicked.connect(lambda: self.call_encrypt_window())

        self.decryption = None
        self.ui.decryption_button.clicked.connect(lambda: self.call_decryption_window())

    def call_encrypt_window(self):
        self.close()
        self.encrypt = Encrypt_window()
        self.encrypt.show()

    def call_decryption_window(self):
        self.close()
        self.decryption = Decryption_Window()
        self.decryption.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = Start_window()
    application.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
