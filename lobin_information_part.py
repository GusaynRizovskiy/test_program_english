# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_information_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(703, 371)
        login.setWindowTitle("Аутентификация")
        self.label_autentification = QtWidgets.QLabel(login)
        self.label_autentification.setGeometry(QtCore.QRect(40, 10, 641, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(26)
        self.label_autentification.setFont(font)
        self.label_autentification.setObjectName("label_autentification")
        self.pbt_enter = QtWidgets.QPushButton(login)
        self.pbt_enter.setGeometry(QtCore.QRect(400, 260, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(16)
        self.pbt_enter.setFont(font)
        self.pbt_enter.setObjectName("pbt_enter")
        self.pbt_close_window = QtWidgets.QPushButton(login)
        self.pbt_close_window.setGeometry(QtCore.QRect(80, 260, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(16)
        self.pbt_close_window.setFont(font)
        self.pbt_close_window.setObjectName("pbt_close_window")
        self.widget = QtWidgets.QWidget(login)
        self.widget.setGeometry(QtCore.QRect(36, 100, 211, 101))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_name = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(16)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.verticalLayout_2.addWidget(self.label_name)
        self.label_surname = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(16)
        self.label_surname.setFont(font)
        self.label_surname.setObjectName("label_surname")
        self.verticalLayout_2.addWidget(self.label_surname)
        self.widget1 = QtWidgets.QWidget(login)
        self.widget1.setGeometry(QtCore.QRect(250, 100, 401, 101))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout.addWidget(self.lineEdit_name)
        self.lineEdit_surname = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_surname.setObjectName("lineEdit_surname")
        self.verticalLayout.addWidget(self.lineEdit_surname)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)
    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Dialog"))
        self.label_autentification.setText(_translate("login", "Аутентификация пользователя"))
        self.pbt_enter.setText(_translate("login", "Войти"))
        self.pbt_close_window.setText(_translate("login", "Закрыть"))
        self.label_name.setText(_translate("login", "Имя"))
        self.label_surname.setText(_translate("login", "Фамилия"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QDialog()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
