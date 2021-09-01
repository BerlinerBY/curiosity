# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trash\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class UiApplication(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(800, 600)
        Window.setStyleSheet("border: None;")
        Window.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(55, 60, 90);")

        """
        add hint-panel
        """
        self.hint = QtWidgets.QFrame(self.centralwidget)
        self.hint.setGeometry(0, 0, 802, 30)
        self.hint.setStyleSheet("background: rgb(55, 60, 90);")

        self.name_app = QtWidgets.QLabel(self.hint)
        self.name_app.setGeometry(20, 0, 100, 30)
        self.name_app.setText("CURIOSITY")
        self.name_app.setStyleSheet("QLabel {"
                                    "   color: rgb(250, 250, 250);"
                                    "}")

        self.close_button = QtWidgets.QPushButton(self.hint)
        self.close_button.setGeometry(770, 0, 30, 30)
        self.close_button.setStyleSheet("QPushButton:hover {"
                                        "   background: rgb(100, 10, 10);"
                                        "   border-radius: 10px;"
                                        "}"
                                        )
        self.close_button.setIcon(QtGui.QIcon("style/close.png"))
        self.close_button.setObjectName("close")

        self.minimize_button = QtWidgets.QPushButton(self.hint)
        self.minimize_button.setGeometry(740, 0, 30, 30)
        self.minimize_button.setStyleSheet("QPushButton {"
                                           "   border-image: url('style/minimize2.png');" 
                                           "}"
                                           "QPushButton:hover {"
                                           "   background: rgb(70, 70, 90);"
                                           "   border-radius: 10px;"
                                           "}"
                                           )
        self.minimize_button.setObjectName("minimize")

        """
        create areas with page
        """
        self.windows = QtWidgets.QTabWidget(self.centralwidget)
        self.windows.setEnabled(True)
        self.windows.setGeometry(QtCore.QRect(0, 30, 802, 602))  # i use 802 and 602 px, because i don`t know, to fix
        # bug with white border of pages
        self.windows.setStyleSheet("QTabBar::tab:hover {"
                                   "    background: rgb(100,100,100);"
                                   "    border-radius: 25px;"
                                   "}"
                                   "QTabBar::tab:selected {"
                                   "    background: rgb(250,250,250);"
                                   "    border-radius: 25px;"
                                   "}"
                                   "QTabBar::tab {"
                                   "    background: rgba(55, 59, 89, 0%);"
                                   "    height: 50px;"
                                   "    width: 50px;"
                                   "    border: none;"
                                   "    margin: 0px;"
                                   "    padding-top: -10px;"
                                   "    padding-bottom: 10px;"
                                   "    padding-left: 3px;"
                                   "}")

        self.windows.setTabPosition(QtWidgets.QTabWidget.West)
        self.windows.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.windows.setTabBarAutoHide(False)  # i can delete this string, but i don`t use this function
        self.windows.setObjectName("windows")

        """
        start page
        """
        self.home = QtWidgets.QWidget()
        self.home.setStyleSheet("QWidget {"
                                "    background-image: url('style/space2.jpg');"
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
        self.created.setGeometry(600, 540, 140, 20)
        self.created.setStyleSheet("QLabel {"
                                   "   background: rgba(0, 0, 0, 0%);"
                                   "   color: rgb(250, 250, 250);"
                                   "   font-size: 15px;"
                                   "}"
                                   )

        """
        page where hide-algorithm start
        """

        style_qlineedit = str("QLineEdit {"
                              "    background-color: rgb(255, 170, 0);"
                              "    border-radius: 10px;"
                              "    font-size: 20px;"
                              "    padding-left: 10px;"
                              "}")
        style_trash_button = str("QPushButton {"
                                 "    border-radius: 20px;"
                                 "    background-color: Transparent;"
                                 "}"
                                 "QPushButton:hover:!pressed {"
                                 "    background: rgb(255, 170, 0);"
                                 "}")

        style_archive_button = str("QPushButton {"
                                   "    border-image: url('style/archive_icon.png');" 
                                   "    border-radius: 20px;"
                                   "    background-color: Transparent;"
                                   "}"
                                   "QPushButton:hover:!pressed {"
                                   "    background: rgb(255, 170, 0);"
                                   "}")

        self.input = QtWidgets.QWidget()
        self.input.setStyleSheet("QWidget {"
                                 "    background-color: rgb(35, 40, 70);"
                                 "}")
        self.input.setObjectName("input")
        self.windows.addTab(self.input, "")

        self.hide_path_to_container = QtWidgets.QLineEdit(self.input)
        self.hide_path_to_container.setGeometry(30, 30, 590, 45)
        self.hide_path_to_container.setPlaceholderText("Please enter container address...")
        self.hide_path_to_container.setStyleSheet(style_qlineedit)
        self.hide_path_to_container.setObjectName("hide_path_to_container")

        self.hide_clear_path = QtWidgets.QPushButton(self.input)
        self.hide_clear_path.setGeometry(QtCore.QRect(625, 30, 45, 45))
        self.hide_clear_path.setStyleSheet(style_trash_button)
        self.hide_clear_path.setIcon(QtGui.QIcon('style/trash_icon.png'))
        self.hide_clear_path.setIconSize(QtCore.QSize(45, 45))
        self.hide_clear_path.setObjectName("hide_clear_path ")

        self.hide_open_container = QtWidgets.QPushButton(self.input)
        self.hide_open_container.setGeometry(QtCore.QRect(675, 30, 45, 45))
        self.hide_open_container.setStyleSheet(style_archive_button)
        self.hide_open_container.setObjectName("hide_open_container")

        self.hide_save_of_file = QtWidgets.QLineEdit(self.input)
        self.hide_save_of_file.setGeometry(QtCore.QRect(30, 105, 590, 45))
        self.hide_save_of_file.setPlaceholderText("Please enter a save address...")
        self.hide_save_of_file.setStyleSheet(style_qlineedit)
        self.hide_save_of_file.setObjectName("hide_save_of_file")

        self.hide_clear_save_of_file = QtWidgets.QPushButton(self.input)
        self.hide_clear_save_of_file.setGeometry(QtCore.QRect(625, 105, 45, 45))
        self.hide_clear_save_of_file.setStyleSheet(style_trash_button)
        self.hide_clear_save_of_file.setIcon(QtGui.QIcon('style/trash_icon.png'))
        self.hide_clear_save_of_file.setIconSize(QtCore.QSize(45, 45))
        self.hide_clear_save_of_file.setObjectName("hide_clear_save_of_file")

        self.hide_save_of_file_button = QtWidgets.QPushButton(self.input)
        self.hide_save_of_file_button.setGeometry(QtCore.QRect(675, 105, 45, 45))
        self.hide_save_of_file_button.setStyleSheet(style_archive_button)
        self.hide_save_of_file_button.setObjectName("hide_save_of_file_button")

        self.hide_text = QtWidgets.QPlainTextEdit(self.input)
        self.hide_text.setPlaceholderText("Please enter text...")
        self.hide_text.setGeometry(QtCore.QRect(30, 180, 590, 120))
        self.hide_text.setStyleSheet("QPlainTextEdit {"
                                     "    background-color: rgb(255, 170, 0);"
                                     "    border-radius: 10px;"
                                     "    font-size: 20px;"
                                     "    padding-left: 10px;"
                                     "}")
        self.hide_text.setObjectName("hide_text")

        self.hide_clear_text = QtWidgets.QPushButton(self.input)
        self.hide_clear_text.setGeometry(QtCore.QRect(625, 180, 95, 120))
        self.hide_clear_text.setStyleSheet(style_trash_button)
        self.hide_clear_text.setIcon(QtGui.QIcon('style/trash_icon.png'))
        self.hide_clear_text.setIconSize(QtCore.QSize(60, 60))
        self.hide_clear_text.setObjectName("hide_clear_text")

        self.hide_progress = QtWidgets.QProgressBar(self.input)
        self.hide_progress.setGeometry(30, 330, 590, 50)
        self.hide_progress.setStyleSheet("background: rgb(28, 181,10);"
                                         "border-radius: 15px;")
        self.hide_progress.setObjectName("hide_progress")

        self.hide_button = QtWidgets.QPushButton(self.input)
        self.hide_button.setGeometry(QtCore.QRect(625, 330, 95, 50))
        self.hide_button.setStyleSheet("QPushButton {"
                                       "    background: rgba(0, 0, 0, 0%);"
                                       "    font-size: 20px;"
                                       "    border-radius: 15px;"
                                       "}"
                                       "QPushButton:hover:!pressed {"
                                       "    background-color: rgb(55, 60, 90);"
                                       "}")
        self.hide_button.setText("Hide")
        self.hide_button.setIcon(QtGui.QIcon('style/hide_icon.png'))
        self.hide_button.setObjectName("hide")

        self.hide_extraction_key = QtWidgets.QTextEdit(self.input)
        self.hide_extraction_key.setGeometry(QtCore.QRect(30, 410, 690, 45))
        self.hide_extraction_key.setStyleSheet("QTextEdit {"
                                               "    background-color: rgb(255, 255, 255);"
                                               "    border-radius: 15px;"
                                               "    font-size: 20px;"
                                               "    padding-top: 8px;"
                                               "    padding-left: 10px;"
                                               "}")
        self.hide_extraction_key.setPlaceholderText("Your recovery key...")
        self.hide_extraction_key.setObjectName("hide_extraction_key")

        self.hide_RSA_key = QtWidgets.QTextEdit(self.input)
        self.hide_RSA_key.setGeometry(QtCore.QRect(30, 490, 690, 45))
        self.hide_RSA_key.setStyleSheet("QTextEdit {"
                                        "    background-color: rgb(255, 255, 255);"
                                        "    border-radius: 15px;"
                                        "    font-size: 20px;"
                                        "    padding-top: 8px;"
                                        "    padding-left: 10px;"
                                        "}")
        self.hide_RSA_key.setPlaceholderText(" Your RSA key...")
        self.hide_RSA_key.setObjectName("hide_RSA_key")

        """
        page where recovery-algorithm start
        """
        self.output = QtWidgets.QWidget()
        self.output.setStyleSheet("QWidget {"
                                  "    background-color: rgb(35, 40, 70);"
                                  "}")
        self.output.setObjectName("output")
        self.windows.addTab(self.output, "")

        """адрес контейнера"""
        self.recovery_path_to_container = QtWidgets.QLineEdit(self.output)
        self.recovery_path_to_container.setGeometry(QtCore.QRect(30, 30, 590, 45))
        self.recovery_path_to_container.setStyleSheet(style_qlineedit)
        self.recovery_path_to_container.setObjectName("recovery_path_to_container")
        self.recovery_path_to_container.setPlaceholderText("Please enter container address...")

        """кнопка отчистки адреса контейнера"""
        self.recovery_clear_path = QtWidgets.QPushButton(self.output)
        self.recovery_clear_path.setGeometry(QtCore.QRect(625, 30, 45, 45))
        self.recovery_clear_path.setStyleSheet(style_trash_button)
        self.recovery_clear_path.setIcon(QtGui.QIcon('style/trash_icon.png'))
        self.recovery_clear_path.setIconSize(QtCore.QSize(45, 45))
        self.recovery_clear_path.setObjectName("recovery_clear_path")

        """кнопка открывающая мои документы для автоматического выбора файла"""
        self.recovery_open_container = QtWidgets.QPushButton(self.output)
        self.recovery_open_container.setGeometry(QtCore.QRect(675, 30, 45, 45))
        self.recovery_open_container.setStyleSheet(style_archive_button)
        self.recovery_open_container.setObjectName("recovery_open_container")

        """поле для ввода ключа извлечения"""
        self.recovery_extraction_key = QtWidgets.QLineEdit(self.output)
        self.recovery_extraction_key.setGeometry(QtCore.QRect(30, 105, 590, 45))
        self.recovery_extraction_key.setStyleSheet(style_qlineedit)
        self.recovery_extraction_key.setObjectName("recovery_extraction_key")
        self.recovery_extraction_key.setPlaceholderText("Please enter your recovery key...")

        """кнопка для отчистки поля с ключом извлечения"""
        self.recovery_clear_extraction_key = QtWidgets.QPushButton(self.output)
        self.recovery_clear_extraction_key.setGeometry(QtCore.QRect(625, 105, 95, 45))
        self.recovery_clear_extraction_key.setStyleSheet(style_trash_button)
        self.recovery_clear_extraction_key.setIcon(QtGui.QIcon('style/trash_icon.png'))
        self.recovery_clear_extraction_key.setIconSize(QtCore.QSize(45, 45))
        self.recovery_clear_extraction_key.setObjectName("recovery_clear_extraction_key")

        """поле для ввода ключа RSA"""
        self.recovery_RSA_key = QtWidgets.QLineEdit(self.output)
        self.recovery_RSA_key.setGeometry(QtCore.QRect(30, 180, 590, 45))
        self.recovery_RSA_key.setStyleSheet(style_qlineedit)
        self.recovery_RSA_key.setObjectName("recovery_RSA_key")
        self.recovery_RSA_key.setPlaceholderText("Please enter your RSA key...")

        """кнопка для отчистки поля с ключом RSA"""
        self.recovery_clear_RSA_key = QtWidgets.QPushButton(self.output)
        self.recovery_clear_RSA_key.setGeometry(QtCore.QRect(625, 180, 95, 45))
        self.recovery_clear_RSA_key.setStyleSheet(style_trash_button)
        self.recovery_clear_RSA_key.setIcon(QtGui.QIcon('style/trash_icon.png'))
        self.recovery_clear_RSA_key.setIconSize(QtCore.QSize(45, 45))
        self.recovery_clear_RSA_key.setObjectName("recovery_clear_RSA_key")

        """поле ввода адреса для сохранения информации"""
        self.recovery_save_of_file = QtWidgets.QLineEdit(self.output)
        self.recovery_save_of_file.setGeometry(QtCore.QRect(30, 255, 590, 45))
        self.recovery_save_of_file.setStyleSheet(style_qlineedit)
        self.recovery_save_of_file.setObjectName("recovery_save_of_file")
        self.recovery_save_of_file.setPlaceholderText("Please enter save-address for container...")

        """кнопка для отчистки поля с адресом сохранения"""
        self.recovery_clean_save_of_file = QtWidgets.QPushButton(self.output)
        self.recovery_clean_save_of_file.setGeometry(QtCore.QRect(625, 255, 45, 45))
        self.recovery_clean_save_of_file.setStyleSheet(style_trash_button)
        self.recovery_clean_save_of_file.setIcon(QtGui.QIcon('style/trash_icon.png'))
        self.recovery_clean_save_of_file.setIconSize(QtCore.QSize(45, 45))
        self.recovery_clean_save_of_file.setObjectName("recovery_clean_save_of_file")

        """кнопка для выбора папки с инфой"""
        self.recovery_open_file = QtWidgets.QPushButton(self.output)
        self.recovery_open_file.setGeometry(QtCore.QRect(675, 255, 45, 45))
        self.recovery_open_file.setStyleSheet(style_archive_button)
        self.recovery_open_file.setObjectName("recovery_open_file")

        """кнопка для запуска алгоритма"""
        self.recovery_Button = QtWidgets.QPushButton(self.output)
        self.recovery_Button.setGeometry(QtCore.QRect(300, 330, 125, 50))
        self.recovery_Button.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                           "border-top-color: rgb(255, 170, 0);\n"
                                           "")
        self.recovery_Button.setObjectName("recovery_Button")

        self.recovery_progress = QtWidgets.QProgressBar(self.output)
        self.recovery_progress.setGeometry(30, 410, 690, 50)
        self.recovery_progress.setStyleSheet("background: rgb(28, 181,10);"
                                             "border-radius: 15px;")
        self.recovery_progress.setObjectName("recovery_progress")

        self.notification = QtWidgets.QTextEdit(self.output)
        self.notification.setGeometry(QtCore.QRect(30, 490, 690, 50))
        self.notification.setStyleSheet("QTextEdit {"
                                        "    background-color: rgb(255, 255, 255);"
                                        "    border-radius: 15px;"
                                        "    font-size: 20px;"
                                        "    padding-top: 8px;"
                                        "    padding-left: 10px;"
                                        "}")
        self.notification.setObjectName("notification")

        """
        page with help-info
        """
        self.support = QtWidgets.QWidget()
        self.support.setStyleSheet("QWidget {"
                                   "    background: rgb(35, 40, 70);"
                                   "}")
        self.support.setObjectName("support")
        self.windows.addTab(self.support, "")

        self.windows.setTabIcon(0, QtGui.QIcon('style/home2.png'))
        self.windows.setTabIcon(1, QtGui.QIcon('style/input.png'))
        self.windows.setTabIcon(2, QtGui.QIcon('style/output.png'))
        self.windows.setTabIcon(3, QtGui.QIcon('style/information.png'))
        self.windows.setIconSize(QtCore.QSize(30, 35))

        Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window)
        self.windows.setCurrentIndex(0)  # не забыть поставить в конце работы 0
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Curiosity"))

        self.recovery_Button.setText(_translate("Window", "Recovery"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = UiApplication()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())
