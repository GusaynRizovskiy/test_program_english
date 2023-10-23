# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'work_information_part.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
class Ui_work_part(object):
    def setupUi(self, work_part):
        work_part.setObjectName("work_part")
        work_part.resize(1122, 624)
        self.label = QtWidgets.QLabel(work_part)
        self.label.setGeometry(QtCore.QRect(220, 10, 741, 61))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_question_label = QtWidgets.QLabel(work_part)
        self.label_question_label.setGeometry(QtCore.QRect(40, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(14)
        self.label_question_label.setFont(font)
        self.label_question_label.setObjectName("label_question_label")
        self.label_question = QtWidgets.QLabel(work_part)
        self.label_question.setGeometry(QtCore.QRect(40, 130, 971, 31))
        self.label_question.setText("")
        self.label_question.setObjectName("label_question")
        self.label_right_unright = QtWidgets.QLabel(work_part)
        self.label_right_unright.setGeometry(QtCore.QRect(40, 380, 150, 30))
        self.label_right_unright.setText("")
        self.label_right_unright.setObjectName("label_right_unright")
        self.label_expression = QtWidgets.QLabel(work_part)
        self.label_expression.setGeometry(QtCore.QRect(40, 430, 1061, 61))
        self.label_expression.setText("")
        self.label_expression.setObjectName("label_expression")
        self.pushButton = QtWidgets.QPushButton(work_part)
        self.pushButton.setGeometry(QtCore.QRect(400, 550, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_number = QtWidgets.QLabel(work_part)
        self.label_number.setGeometry(QtCore.QRect(210, 90, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(14)
        self.label_number.setFont(font)
        self.label_number.setObjectName("label_number")
        self.label_number_question = QtWidgets.QLabel(work_part)
        self.label_number_question.setGeometry(QtCore.QRect(310, 90, 51, 31))
        self.label_number_question.setText("")
        self.label_number_question.setObjectName("label_number_question")
        self.widget = QtWidgets.QWidget(work_part)
        self.widget.setGeometry(QtCore.QRect(40, 170, 1001, 171))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rdb_1 = QtWidgets.QRadioButton(self.widget)
        self.rdb_1.setText("")
        self.rdb_1.setObjectName("rdb_1")
        self.verticalLayout.addWidget(self.rdb_1)
        self.rdb_2 = QtWidgets.QRadioButton(self.widget)
        self.rdb_2.setText("")
        self.rdb_2.setObjectName("rdb_2")
        self.verticalLayout.addWidget(self.rdb_2)
        self.rdb_3 = QtWidgets.QRadioButton(self.widget)
        self.rdb_3.setText("")
        self.rdb_3.setObjectName("rdb_3")
        self.verticalLayout.addWidget(self.rdb_3)
        self.rdb_1.setFont(QFont("Aesthetic",14))
        self.rdb_2.setFont(QFont("Aesthetic", 14))
        self.rdb_3.setFont(QFont("Aesthetic", 14))
        self.label_question.setFont(QFont("Aesthetic", 14))
        self.label_number_question.setFont(QFont("Aesthetic", 14))
        self.label_expression.setFont(QFont("Aesthetic", 14))
        self.label_right_unright.setFont(QFont("Aesthetic", 14))
        self.retranslateUi(work_part)
        self.rdb_1.hide()
        self.rdb_2.hide()
        self.rdb_3.hide()
        QtCore.QMetaObject.connectSlotsByName(work_part)
    def retranslateUi(self, work_part):
        _translate = QtCore.QCoreApplication.translate
        work_part.setWindowTitle(_translate("work_part", "Dialog"))
        self.label.setText(_translate("work_part", "Тест по английскому языку"))
        self.label_question_label.setText(_translate("work_part", "Вопрос:"))
        self.pushButton.setText(_translate("work_part", "Дальше"))
        self.label_number.setText(_translate("work_part", "Номер:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    work_part = QtWidgets.QDialog()
    ui = Ui_work_part()
    ui.setupUi(work_part)
    work_part.show()
    sys.exit(app.exec_())
