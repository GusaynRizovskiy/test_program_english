import re
from PyQt5.QtWidgets import QMessageBox
def process(self,username,surname,login_window):
    if re.fullmatch(r'[а-яА-яa-zA-Z]+',username) and re.fullmatch(r'[а-яА-яa-zA-Z]+',surname):
        print("correct")
        self.work_part()
    else:
        mess_box = QMessageBox()
        mess_box.setWindowTitle("Предупреждение")
        mess_box.setText("Некорректные данные")
        mess_box.setInformativeText("Введите фамилию и имя правильно")
        mess_box.setIcon(QMessageBox.Warning)
        mess_box.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        mess_box.show()
        mess_box.exec_()
        print("incorrect")
