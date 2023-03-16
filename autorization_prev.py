# Form implementation generated from reading ui file 'autorization.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AuthWindow(object):
    def setupUi(self, AuthWindow):
        AuthWindow.setObjectName("AuthWindow")
        AuthWindow.setEnabled(True)
        AuthWindow.resize(375, 368)
        AuthWindow.setMinimumSize(QtCore.QSize(375, 368))
        AuthWindow.setMaximumSize(QtCore.QSize(375, 368))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        AuthWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/ProgrammIcon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        AuthWindow.setWindowIcon(icon)
        AuthWindow.setStyleSheet("background-color: rgb(17, 17, 17);")
        AuthWindow.setSizeGripEnabled(False)
        self.auth_button = QtWidgets.QPushButton(parent=AuthWindow)
        self.auth_button.setGeometry(QtCore.QRect(10, 320, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.auth_button.setFont(font)
        self.auth_button.setStyleSheet("QPushButton::hover{\n"
"background-color: rgb(194, 194, 194);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(83, 83, 83);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.auth_button.setObjectName("auth_button")
        self.exit_button = QtWidgets.QPushButton(parent=AuthWindow)
        self.exit_button.setGeometry(QtCore.QRect(280, 320, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("QPushButton::hover{\n"
"background-color: rgb(194, 194, 194);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(83, 83, 83);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.exit_button.setObjectName("exit_button")
        self.authorization_label = QtWidgets.QLabel(parent=AuthWindow)
        self.authorization_label.setGeometry(QtCore.QRect(0, 40, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.authorization_label.setFont(font)
        self.authorization_label.setStyleSheet("background-color: rgb(30, 185, 85);\n"
"color: rgb(255, 255, 255);")
        self.authorization_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.authorization_label.setObjectName("authorization_label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=AuthWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 284, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.login_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.login_layout.setContentsMargins(0, 0, 0, 0)
        self.login_layout.setObjectName("login_layout")
        self.login_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.login_label.setFont(font)
        self.login_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.login_label.setObjectName("login_label")
        self.login_layout.addWidget(self.login_label)
        self.login_lineEdit = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.login_lineEdit.setFont(font)
        self.login_lineEdit.setStyleSheet("QLineEdit::hover{\n"
"background-color: rgb(54, 54, 54);\n"
"}\n"
"QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(83, 83, 83);\n"
"}")
        self.login_lineEdit.setText("")
        self.login_lineEdit.setFrame(True)
        self.login_lineEdit.setObjectName("login_lineEdit")
        self.login_layout.addWidget(self.login_lineEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=AuthWindow)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 190, 281, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.password_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.password_layout.setContentsMargins(0, 0, 0, 0)
        self.password_layout.setObjectName("password_layout")
        self.password_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.password_label.setObjectName("password_label")
        self.password_layout.addWidget(self.password_label)
        self.password_lineEdit = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Gotham Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setStyleSheet("QLineEdit::hover{\n"
"background-color: rgb(54, 54, 54);\n"
"}\n"
"QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(83, 83, 83);\n"
"}")
        self.password_lineEdit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhHiddenText|QtCore.Qt.InputMethodHint.ImhNoAutoUppercase|QtCore.Qt.InputMethodHint.ImhNoPredictiveText|QtCore.Qt.InputMethodHint.ImhSensitiveData)
        self.password_lineEdit.setText("")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.password_layout.addWidget(self.password_lineEdit)
        self.error_label = QtWidgets.QLabel(parent=AuthWindow)
        self.error_label.setEnabled(True)
        self.error_label.setGeometry(QtCore.QRect(20, 280, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.error_label.setFont(font)
        self.error_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.error_label.setObjectName("error_label")
        self.title_bar = QtWidgets.QFrame(parent=AuthWindow)
        self.title_bar.setGeometry(QtCore.QRect(0, 0, 375, 41))
        self.title_bar.setMouseTracking(True)
        self.title_bar.setTabletTracking(False)
        self.title_bar.setAcceptDrops(True)
        self.title_bar.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;")
        self.title_bar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.title_bar.setObjectName("title_bar")
        self.close_button = QtWidgets.QPushButton(parent=self.title_bar)
        self.close_button.setGeometry(QtCore.QRect(1890, 10, 31, 20))
        self.close_button.setStyleSheet("border-radius: 2px;\n"
"")
        self.close_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/window/icons/close_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.close_button.setIcon(icon1)
        self.close_button.setIconSize(QtCore.QSize(13, 13))
        self.close_button.setObjectName("close_button")
        self.hide_button = QtWidgets.QPushButton(parent=self.title_bar)
        self.hide_button.setGeometry(QtCore.QRect(1860, 10, 31, 20))
        self.hide_button.setStyleSheet("border-radius: 2px;\n"
"")
        self.hide_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/window/icons/hide_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.hide_button.setIcon(icon2)
        self.hide_button.setIconSize(QtCore.QSize(25, 25))
        self.hide_button.setObjectName("hide_button")
        self.close_button_2 = QtWidgets.QPushButton(parent=self.title_bar)
        self.close_button_2.setGeometry(QtCore.QRect(340, 10, 31, 20))
        self.close_button_2.setStyleSheet("QPushButton::hover{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(83, 83, 83);\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.close_button_2.setText("")
        self.close_button_2.setIcon(icon1)
        self.close_button_2.setIconSize(QtCore.QSize(13, 13))
        self.close_button_2.setObjectName("close_button_2")
        self.hide_button_2 = QtWidgets.QPushButton(parent=self.title_bar)
        self.hide_button_2.setGeometry(QtCore.QRect(300, 10, 31, 21))
        self.hide_button_2.setStyleSheet("QPushButton::hover{\n"
"background-color: rgb(121, 121, 121);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(83, 83, 83);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"")
        self.hide_button_2.setText("")
        self.hide_button_2.setIcon(icon2)
        self.hide_button_2.setIconSize(QtCore.QSize(25, 25))
        self.hide_button_2.setObjectName("hide_button_2")
        self.auth_button.raise_()
        self.exit_button.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.error_label.raise_()
        self.title_bar.raise_()
        self.authorization_label.raise_()

        self.retranslateUi(AuthWindow)
        QtCore.QMetaObject.connectSlotsByName(AuthWindow)

    def retranslateUi(self, AuthWindow):
        _translate = QtCore.QCoreApplication.translate
        AuthWindow.setWindowTitle(_translate("AuthWindow", "Voice journal"))
        self.auth_button.setText(_translate("AuthWindow", "Авторизироваться"))
        self.exit_button.setText(_translate("AuthWindow", "Выйти"))
        self.authorization_label.setText(_translate("AuthWindow", "Авторизация"))
        self.login_label.setText(_translate("AuthWindow", "Логин"))
        self.password_label.setText(_translate("AuthWindow", "Пароль"))
        self.error_label.setText(_translate("AuthWindow", "Ошибка авторизации!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AuthWindow = QtWidgets.QDialog()
    ui = Ui_AuthWindow()
    ui.setupUi(AuthWindow)
    AuthWindow.show()
    sys.exit(app.exec())
