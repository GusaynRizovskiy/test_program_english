import sys
from PyQt5 import QtWidgets, uic
from lobin_information_part import Ui_login
from work_information_part import Ui_work_part
import re
from PyQt5.QtWidgets import  QMessageBox
import json

class Form1(QtWidgets.QMainWindow, Ui_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pbt_enter.clicked.connect(self.open_form2)
    def open_form2(self):
        self.username = self.lineEdit_name.text()
        self.surname = self.lineEdit_name.text()
        if re.fullmatch(r'[а-яА-яa-zA-Z]+', self.username) and re.fullmatch(r'[а-яА-яa-zA-Z]+',self.surname):
            print("correct")
            self.form2 = Form2()
            self.form2.show()
        else:
            mess_box = QMessageBox()
            mess_box.setWindowTitle("Предупреждение")
            mess_box.setText("Некорректные данные")
            mess_box.setInformativeText("Введите фамилию и имя правильно")
            mess_box.setIcon(QMessageBox.Warning)
            mess_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            mess_box.show()
            mess_box.exec_()
            print("incorrect")



class Form2(QtWidgets.QMainWindow, Ui_work_part):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.open_file()
        self.pushButton.clicked.connect(self.next_questinon)
    def open_file(self):
        with open("Test.json","r",encoding="utf-8-sig") as new_file:
            self.data = json.load(new_file)
            self.k = 0

    def next_questinon(self):
        self.label_number_question.setText(self.data["вопросы"][self.k]["Номер вопроса"])
        self.label_question.setText(self.data["вопросы"][self.k]["Вопрос"])
        self.rdb_1.setText(self.data["вопросы"][self.k]["Вариант ответа 1"])
        self.rdb_2.setText(self.data["вопросы"][self.k]["Вариант ответа 2"])
        self.rdb_3.setText(self.data["вопросы"][self.k]["Вариант ответа 3"])
        self.k+=1

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form1 = Form1()
    form1.show()
    sys.exit(app.exec_())