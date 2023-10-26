import sys
from PyQt5 import QtWidgets, uic
from lobin_information_part import Ui_login
from work_information_part import Ui_work_part
from finish_work import Ui_finish_part
import re
from PyQt5.QtWidgets import  QMessageBox
import json
from PyQt5.QtGui import QPalette, QBrush, QPixmap
class Form1(QtWidgets.QMainWindow, Ui_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pbt_enter.clicked.connect(self.open_form2)
        self.pbt_close_window.clicked.connect(self.close_form1)
    def open_form2(self):
        self.username = self.lineEdit_name.text()
        self.surname = self.lineEdit_surname.text()
        if re.fullmatch(r'[а-яА-яa-zA-Z]+', self.username) and re.fullmatch(r'[а-яА-яa-zA-Z]+',self.surname):
            form1.close()
            self.form2 = Form2()
            palette = QPalette()
            palette.setBrush(QPalette.Background, QBrush(QPixmap("./1614582859_27-p-belii-fon-sovremennii-31.jpg")))
            self.form2.setPalette(palette)
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
    def close_form1(self):
        self.close()



class Form2(QtWidgets.QMainWindow, Ui_work_part):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.setText("Начать")
        self.open_file()
        self.pushButton.clicked.connect(self.next_questinon)
    def open_file(self):
        with open("Test.json","r",encoding="utf-8-sig") as new_file:
            self.data = json.load(new_file)
            self.k = 0
            self.q = 0
    def next_questinon(self):
        if self.k == 20:
            self.pushButton.setText("Закончить")
            self.form3 = Form3(self.q)
            palette = QPalette()
            palette.setBrush(QPalette.Background,
            QBrush(QPixmap("./1666346768_22-mykaleidoscope-ru-p-kipelno-belii-oboi-25.jpg")))
            self.form3.setPalette(palette)
            self.form3.show()
            form1.form2.close()
        else:
            self.rdb_1.show()
            self.rdb_2.show()
            self.rdb_3.show()
            self.pushButton.setText("Дальше")
            self.label_number_question.setText(self.data["вопросы"][self.k]["Номер вопроса"])
            self.label_question.setText(self.data["вопросы"][self.k]["Вопрос"])
            self.rdb_1.setText(self.data["вопросы"][self.k]["Вариант ответа 1"])
            self.rdb_2.setText(self.data["вопросы"][self.k]["Вариант ответа 2"])
            self.rdb_3.setText(self.data["вопросы"][self.k]["Вариант ответа 3"])
            if self.rdb_1.isChecked() or self.rdb_2.isChecked() or self.rdb_3.isChecked():
                self.show_answer()
                self.k+=1


    def show_answer(self):
        if self.rdb_1.isChecked():
            if self.rdb_1.text() == self.data["вопросы"][self.k]["Правильный ответ"]:
                self.label_right_unright.setText("Правильно")
                self.label_right_unright.setStyleSheet("background-color: green;border: 1px solid black;")
                self.q+=1
            else:
                self.label_right_unright.setText("Неправильно")
                self.label_expression.setText(self.data["вопросы"][self.k]["Правильный ответ"])
                self.label_right_unright.setStyleSheet("background-color: red;border: 1px solid black;")
        elif self.rdb_2.isChecked():
            if self.rdb_2.text() == self.data["вопросы"][self.k]["Правильный ответ"]:
                self.label_right_unright.setText("Правильно")
                self.label_right_unright.setStyleSheet("background-color: green;border: 1px solid black;")
                self.q += 1
            else:
                self.label_right_unright.setText("Неправильно")
                self.label_expression.setText(self.data["вопросы"][self.k]["Правильный ответ"])
                self.label_right_unright.setStyleSheet("background-color: red;border: 1px solid black;")
        elif self.rdb_3.isChecked():
            if self.rdb_3.text() == self.data["вопросы"][self.k]["Правильный ответ"]:
                self.label_right_unright.setText("Правильно")
                self.label_right_unright.setStyleSheet("background-color: green;border: 1px solid black;")
                self.q += 1
            else:
                self.label_right_unright.setText("Неправильно")
                self.label_expression.setText(self.data["вопросы"][self.k]["Правильный ответ"])
                self.label_right_unright.setStyleSheet("background-color: red;border: 1px solid black;")

class Form3(QtWidgets.QMainWindow,Ui_finish_part):
    def __init__(self,q):
        self.q = q
        super().__init__()
        self.setupUi(self)
        self.label_right_answer.setText(str(self.q))
        if q>18:
            self.label_mark.setText("5")
        elif q>15 and q<19:
            self.label_mark.setText("4")
        elif q>11 and q<16:
            self.label_mark.setText("3")
        else:
            self.label_mark.setText("2")
        self.pbt_finish.clicked.connect(self.function_close)
        self.pbt_back.setEnabled(False)
    def function_close(self):
        self.close()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form1 = Form1()
    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(QPixmap("./auth.jpg")))
    form1.setPalette(palette)
    form1.show()
    sys.exit(app.exec_())