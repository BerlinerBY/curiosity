# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trash\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("border: None;")
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(55, 59, 89);")

        """
        add hint-panel
        """
        self.hint = QtWidgets.QFrame(self.centralwidget)
        self.hint.setGeometry(0, 0, 802, 30)
        self.hint.setStyleSheet("background: rgb(50, 50, 70);")

        self.name_app = QtWidgets.QLabel(self.hint)
        self.name_app.setGeometry(20, 0, 100, 30)
        self.name_app.setText("CURIOSITY")
        self.name_app.setStyleSheet("QLabel {"
                                    "   color: rgb(250, 250, 250);"
                                    "}")

        self.close_button = QtWidgets.QPushButton(self.hint)
        self.close_button.setGeometry(770, 0, 30, 30)
        self.close_button.setStyleSheet("QPushButton {"
                                        "   border-image: url('style/close.png');"
                                        "}"
                                        "QPushButton:hover {"
                                        "   background: rgb(100, 10, 10);"
                                        "   border-radius: 10px;"
                                        "}"
                                        )
        self.close_button.setObjectName("close")

        self.minimize_button = QtWidgets.QPushButton(self.hint)
        self.minimize_button.setGeometry(740, 0, 30, 30)
        self.minimize_button.setStyleSheet("QPushButton {"
                                           "   border-image: url('style/minimize2.png');"
                                           "}"
                                           "QPushButton:hover {"
                                           "   background: rgb(100, 10, 10);"
                                           "   border-radius: 10px;"
                                           "}"
                                           )
        self.minimize_button.setObjectName("minimize")

        """
        create areas with page
        """
        self.windows = QtWidgets.QTabWidget(self.centralwidget)
        self.windows.setEnabled(True)
        self.windows.setGeometry(
            QtCore.QRect(0, 30, 802, 602))  # i use 802 and 602 px, because i don`t know, to fix bug
                                            # with white border of pages
        self.windows.setStyleSheet("QTabBar::tab { "
                                   "    width: 50px; "
                                   "    height: 50px; "
                                   "    background: rgb(55, 59, 89);"
                                   "}"
                                   "QTabBar::tab:hover {"
                                   "    background: rgb(100,100,100);"
                                   "    border-radius: 20px;"
                                   "}"
                                   "QTabBar::tab:selected {"
                                   "    background: rgb(250,250,250);"
                                   "    border-radius: 20px;"
                                   "}"
                                   )

        self.windows.setTabPosition(QtWidgets.QTabWidget.West)
        self.windows.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.windows.setTabBarAutoHide(False)  # i can delete this string, but i don`t use this function
        self.windows.setObjectName("windows")

        """
        start page
        """
        self.home = QtWidgets.QWidget()
        self.home.setStyleSheet("QWidget {"
                                "    background-image: url('style/space.jpg');"
                                "    border: None;"
                                "}"
                                )
        self.home.setObjectName("home")
        self.windows.addTab(self.home, "")

        self.welcom_lable = QtWidgets.QLabel(self.home)
        self.welcom_lable.setText("Welcome to Curiosity")
        self.welcom_lable.setGeometry(75, 120, 600, 100)
        self.welcom_lable.setStyleSheet("QLabel {"
                                        "   background: rgba(100, 100, 100, 30%);"
                                        "   color: rgb(250, 250, 250);"
                                        "   font-size: 40px;"
                                        "   border-radius: 50px;"
                                        "}"
                                        )
        self.welcom_lable.setAlignment(QtCore.Qt.AlignCenter)

        self.short_info = QtWidgets.QLabel(self.home)
        self.short_info.setText("   This is a little program\n"
                                "   It will help you protect your information")
        self.short_info.setGeometry(115, 270, 520, 100)
        self.short_info.setStyleSheet("QLabel {"
                                      "   background: rgba(100, 100, 100, 30%);"
                                      "   color: rgb(250, 250, 250);"
                                      "   font-size: 25px;"
                                      "   border-radius: 25px;"
                                      "}"
                                      )

        self.created = QtWidgets.QLabel(self.home)
        self.created.setText("Created: BerlinerBY")
        self.created.setGeometry(620, 550, 130, 20)
        self.created.setStyleSheet("QLabel {"
                                   "   background: rgba(0, 0, 0, 0%);"
                                   "   color: rgb(250, 250, 250);"
                                   "   font-size: 15px;"
                                   "}"
                                   )

        """
        page where hide-algorithm start
        """
        self.input = QtWidgets.QWidget()
        self.input.setStyleSheet("QWidget {\n"
                                 "    background-color: rgb(177, 40, 255);\n"
                                 "}")
        self.input.setObjectName("input")
        self.windows.addTab(self.input, "")

        self.input_adress_file = QtWidgets.QLineEdit(self.input)
        self.input_adress_file.setGeometry(30, 30, 270, 25)
        self.input_adress_file.setPlaceholderText(" Please enter container address...")
        self.input_adress_file.setStyleSheet("QLineEdit {"
                                             "    background-color: rgb(255, 170, 0);"
                                             "    border: none;"
                                             "}")
        self.input_adress_file.setObjectName("input_adress_file")

        self.clear_line_adress = QtWidgets.QPushButton(self.input)
        self.clear_line_adress.setGeometry(QtCore.QRect(300, 30, 50, 25))
        self.clear_line_adress.setStyleSheet("QPushButton {"
                                             "  background-color: rgb(80, 100, 127);"
                                             "  border: 2px solid rgb(250, 250, 250);"
                                             "}"
                                             "QPushButton:hover:!pressed {"
                                             "  border: 2px solid rgb(100, 100, 100);"
                                             "}"
                                             "QPushButton:pressed {"
                                             "  background: rgb(70, 100, 117);"
                                             "}")
        self.clear_line_adress.setObjectName("clear")

        self.open_file = QtWidgets.QPushButton(self.input)
        self.open_file.setGeometry(QtCore.QRect(350, 30, 75, 25))
        self.open_file.setStyleSheet("background-color: rgb(80, 100, 127);")
        self.open_file.setObjectName("open_file")

        self.input_save_adress_file = QtWidgets.QLineEdit(self.input)
        self.input_save_adress_file.setGeometry(QtCore.QRect(30, 85, 270, 25))
        self.input_save_adress_file.setPlaceholderText(" Please enter a save address...")
        self.input_save_adress_file.setStyleSheet("QLineEdit {\n"
                                                  "    background-color: rgb(255, 170, 0);\n"
                                                  "    border: None;\n"
                                                  "}")
        self.input_save_adress_file.setObjectName("input_save_adress_file")

        self.clear_save_line_adress = QtWidgets.QPushButton(self.input)
        self.clear_save_line_adress.setGeometry(QtCore.QRect(300, 85, 50, 25))
        self.clear_save_line_adress.setStyleSheet("background-color: rgb(80, 100, 127);")
        self.clear_save_line_adress.setObjectName("clear")

        self.save_file = QtWidgets.QPushButton(self.input)
        self.save_file.setGeometry(QtCore.QRect(350, 85, 75, 25))
        self.save_file.setStyleSheet("background-color: rgb(80, 100, 127);")
        self.save_file.setObjectName("save_file")

        self.input_text = QtWidgets.QPlainTextEdit(self.input)
        self.input_text.setPlaceholderText("Please enter text...")
        self.input_text.setGeometry(QtCore.QRect(450, 30, 270, 230))
        self.input_text.setStyleSheet("QPlainTextEdit {"
                                      "    background-color: rgb(255, 170, 0);"
                                      "    border: None;"
                                      "}")
        self.input_text.setObjectName("input_text")

        self.clear_input_text = QtWidgets.QPushButton(self.input)
        self.clear_input_text.setGeometry(QtCore.QRect(450, 285, 125, 25))
        self.clear_input_text.setStyleSheet("background-color: rgb(80, 100, 127);")
        self.clear_input_text.setObjectName("clear_button")

        self.hide_button = QtWidgets.QPushButton(self.input)
        self.hide_button.setGeometry(QtCore.QRect(300, 140, 125, 25))
        self.hide_button.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.hide_button.setObjectName("hide")

        self.hide_progress = QtWidgets.QProgressBar(self.input)
        self.hide_progress.setGeometry(30, 200, 390, 30)
        self.hide_progress.setStyleSheet("background: rgb(28, 181,10);")
        self.hide_progress.setObjectName("hide_progress")

        self.output_recovery_key = QtWidgets.QTextEdit(self.input)
        self.output_recovery_key.setGeometry(QtCore.QRect(30, 350, 390, 30))
        self.output_recovery_key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.output_recovery_key.setObjectName("output_key")
        self.output_recovery_key.setPlaceholderText("Your recovery key...")

        self.output_RSA_key = QtWidgets.QTextEdit(self.input)
        self.output_RSA_key.setGeometry(QtCore.QRect(30, 410, 390, 30))
        self.output_RSA_key.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.output_RSA_key.setObjectName("output_key")
        self.output_RSA_key.setPlaceholderText("Your RSA key...")

        """
        page where recovery-algorithm start
        """
        self.output = QtWidgets.QWidget()
        self.output.setStyleSheet("QWidget {"
                                  "    background-color: rgb(77, 40, 255);"
                                  "}")
        self.output.setObjectName("output")
        self.windows.addTab(self.output, "")

        """адрес контейнера"""
        self.input_line_adress = QtWidgets.QLineEdit(self.output)
        self.input_line_adress.setGeometry(QtCore.QRect(30, 60, 270, 30))
        self.input_line_adress.setStyleSheet("background-color: rgb(170, 85, 127);\n"
                                             "border-color: rgb(255, 170, 0);")
        self.input_line_adress.setObjectName("input_line_adress")
        self.input_line_adress.setPlaceholderText(" Enter container adress...")

        """кнопка отчистки адреса контейнера"""
        self.clear_line_adress_Button = QtWidgets.QPushButton(self.output)
        self.clear_line_adress_Button.setGeometry(QtCore.QRect(300, 60, 50, 30))
        self.clear_line_adress_Button.setStyleSheet("background-color: rgb(80, 100, 127);")
        self.clear_line_adress_Button.setObjectName("clear")

        """кнопка открывающая мои документы для автоматического выбора файла"""
        self.input_adress_Button = QtWidgets.QPushButton(self.output)
        self.input_adress_Button.setGeometry(QtCore.QRect(350, 60, 75, 30))
        self.input_adress_Button.setStyleSheet("background-color: rgb(80, 100, 127);")
        self.input_adress_Button.setObjectName("input_adress_Button")

        """поле для ввода ключа извлечения"""
        self.input_line_recovery_key = QtWidgets.QLineEdit(self.output)
        self.input_line_recovery_key.setGeometry(QtCore.QRect(30, 120, 320, 30))
        self.input_line_recovery_key.setStyleSheet("border-color: rgb(255, 85, 0);\n"
                                                     "background-color: rgb(170, 85, 127);")
        self.input_line_recovery_key.setObjectName("input_line_key")
        self.input_line_recovery_key.setPlaceholderText(" Enter your recovery key...")

        """кнопка для отчистки поля с ключом извлечения"""
        self.clear_line_recovery_key_Button = QtWidgets.QPushButton(self.output)
        self.clear_line_recovery_key_Button.setGeometry(QtCore.QRect(350, 120, 75, 30))
        self.clear_line_recovery_key_Button.setStyleSheet("background-color: rgb(80, 100, 127);")
        self.clear_line_recovery_key_Button.setObjectName("clear_line_key")

        """поле для ввода ключа RSA"""
        self.input_line_RSA_key = QtWidgets.QLineEdit(self.output)
        self.input_line_RSA_key.setGeometry(QtCore.QRect(30, 180, 320, 30))
        self.input_line_RSA_key.setStyleSheet("border-color: rgb(255, 85, 0);\n"
                                              "background-color: rgb(170, 85, 127);")
        self.input_line_RSA_key.setObjectName("input_line_key")
        self.input_line_RSA_key.setPlaceholderText(" Enter your RSA key...")

        """кнопка для отчистки поля с ключом RSA"""
        self.clear_line_RSA_key_Button = QtWidgets.QPushButton(self.output)
        self.clear_line_RSA_key_Button.setGeometry(QtCore.QRect(350, 180, 75, 30))
        self.clear_line_RSA_key_Button.setStyleSheet("background-color: rgb(80, 100, 127);")
        self.clear_line_RSA_key_Button.setObjectName("clear_line_RSA_key")

        """поле ввода адреса для сохранения информации"""
        self.input_line_save_adress = QtWidgets.QLineEdit(self.output)
        self.input_line_save_adress.setGeometry(QtCore.QRect(30, 240, 270, 30))
        self.input_line_save_adress.setStyleSheet("border-color: rgb(255, 85, 0);\n"
                                                  "background-color: rgb(170, 85, 127);")
        self.input_line_save_adress.setObjectName("input_line_save_adress")
        self.input_line_save_adress.setPlaceholderText(" Enter save-adress for container...")

        """кнопка для выбора папки с инфой"""
        self.input_save_adress_Button = QtWidgets.QPushButton(self.output)
        self.input_save_adress_Button.setGeometry(QtCore.QRect(350, 240, 75, 30))
        self.input_save_adress_Button.setStyleSheet("background-color: rgb(80, 100, 127);\n"
                                                    "border-top-color: rgb(255, 170, 0);\n"
                                                    "")
        self.input_save_adress_Button.setObjectName("input_save_adress_Button")

        """кнопка для отчистки поля с адресом сохранения"""
        self.clear_line_save_adress_Button = QtWidgets.QPushButton(self.output)
        self.clear_line_save_adress_Button.setGeometry(QtCore.QRect(300, 240, 50, 30))
        self.clear_line_save_adress_Button.setStyleSheet("background-color: rgb(80, 100, 127);\n"
                                                         "border-top-color: rgb(255, 170, 0);\n"
                                                         "")
        self.clear_line_save_adress_Button.setObjectName("clear_save_line")

        """кнопка для запуска алгоритма"""
        self.recovery_Button = QtWidgets.QPushButton(self.output)
        self.recovery_Button.setGeometry(QtCore.QRect(300, 300, 125, 30))
        self.recovery_Button.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                             "border-top-color: rgb(255, 170, 0);\n"
                                             "")
        self.recovery_Button.setObjectName("recovery_Button")

        self.ending = QtWidgets.QTextEdit(self.output)
        self.ending.setGeometry(QtCore.QRect(30, 360, 395, 30))
        self.ending.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ending.setObjectName("ending")

        """
        page with help-info
        """
        self.support = QtWidgets.QWidget()
        self.support.setStyleSheet("QWidget {"
                                   "    background-color: rgb(77, 140, 255);"
                                   "}")
        self.support.setObjectName("support")
        self.windows.addTab(self.support, "")

        self.windows.setTabIcon(0, QtGui.QIcon('style/home-icon.png'))
        self.windows.setTabIcon(1, QtGui.QIcon('style/input.png'))
        self.windows.setTabIcon(2, QtGui.QIcon('style/output.png'))
        self.windows.setTabIcon(3, QtGui.QIcon('style/help.png'))

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.windows.setCurrentIndex(2)  # не забыть поставить в конце работы 0
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.clear_line_adress.setText(_translate("MainWindow", "Clear"))
        self.open_file.setText(_translate("MainWindow", "Chek file"))
        self.clear_save_line_adress.setText(_translate("MainWindow", "Clear"))
        self.save_file.setText(_translate("MainWindow", "Chek save"))
        self.hide_button.setText(_translate("MainWindow", "Hide"))
        self.clear_input_text.setText(_translate("MainWindow", "Clear"))

        self.clear_line_adress_Button.setText(_translate("MainWindow", "Clear"))
        self.input_adress_Button.setText(_translate("MainWindow", "Chek file"))
        self.input_save_adress_Button.setText(_translate("MainWindow", "Chek file"))
        self.clear_line_save_adress_Button.setText(_translate("MainWindow", "Clear"))
        self.clear_line_recovery_key_Button.setText(_translate("MainWindow", "Clear"))
        self.clear_line_RSA_key_Button.setText(_translate("MainWindow", "Clear"))
        self.recovery_Button.setText(_translate("MainWindow", "Recovery"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
