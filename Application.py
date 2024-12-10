import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, \
    QLabel, QMainWindow, QTableWidgetItem

f = 'project.sqlite3'
con = sqlite3.connect(f)
cur = con.cursor()


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 400, 300, 200)
        self.lbl = QLabel(self)
        self.lbl.setText('Выберите опцию:')
        self.lbl.move(100, 10)
        self.btn1 = QPushButton('Забронировать билет', self)
        self.btn1.resize(150, 50)
        self.btn1.move(75, 50)
        self.btn1.clicked.connect(self.run1)
        self.btn2 = QPushButton('Посмотреть расписание', self)
        self.btn2.resize(150, 50)
        self.btn2.move(75, 125)
        self.btn2.clicked.connect(self.run2)

    def run1(self):
        self.close()
        self.ex1 = TakingTicketStartCity(self)
        self.ex1.show()

    def run2(self):
        pass


class TakingTicketStartCity(QWidget):
    def __init__(self, window1):
        super().__init__()
        self.initUI()
        self.window = window1

    def initUI(self):
        self.setGeometry(300, 300, 300, 250)
        self.lbl = QLabel(self)
        self.lbl.move(75, 10)
        self.lbl.setText('Введите пункт вылета(город):')
        self.field = QLineEdit(self)
        self.field.resize(150, 50)
        self.field.move(75, 30)
        self.lbl1 = QLabel(self)
        self.lbl1.move(75, 80)
        self.lbl1.resize(200, 30)
        self.btn1 = QPushButton('Далее', self)
        self.btn1.resize(150, 50)
        self.btn1.move(75, 110)
        self.btn1.clicked.connect(self.run1)
        self.btn2 = QPushButton('Назад', self)
        self.btn2.resize(150, 50)
        self.btn2.move(75, 180)
        self.btn2.clicked.connect(self.run2)

    def run1(self):
        con = sqlite3.connect(f)
        cur = con.cursor()
        c = self.field.text()
        self.start_city = c
        self.close()
        self.ex1 = TakingTicketFinishCity(self, self.start_city)
        self.ex1.show()

    def run2(self):
        self.close()
        self.window.show()


class TakingTicketFinishCity(QWidget):
    def __init__(self, window2, start_city):
        super().__init__()
        self.initUI()
        self.window = window2
        self.start_city = start_city

    def initUI(self):
        self.setGeometry(300, 300, 300, 250)
        self.lbl = QLabel(self)
        self.lbl.move(75, 10)
        self.lbl.setText('Введите пункт назначения(город):')
        self.field = QLineEdit(self)
        self.field.resize(150, 50)
        self.field.move(75, 30)
        self.lbl1 = QLabel(self)
        self.lbl1.move(75, 80)
        self.lbl1.resize(200, 30)
        self.btn1 = QPushButton('Далее', self)
        self.btn1.resize(150, 50)
        self.btn1.move(75, 110)
        self.btn1.clicked.connect(self.run1)
        self.btn2 = QPushButton('Назад', self)
        self.btn2.resize(150, 50)
        self.btn2.move(75, 180)
        self.btn2.clicked.connect(self.run2)

    def run1(self):
        con = sqlite3.connect(f)
        cur = con.cursor()
        c = self.field.text()
        self.finish_city = c
        self.close()
        self.ex1 = TakingTicketDatetime(self, self.start_city, self.finish_city)
        self.ex1.show()

    def run2(self):
        self.close()
        self.window.show()


class TakingTicketDatetime(QWidget):
    def __init__(self, window, start_city, finish_city):
        super().__init__()
        self.initUI()
        self.window = window
        self.start_city = start_city
        self.finish_city = finish_city

    def initUI(self):
        self.setGeometry(300, 300, 300, 250)
        self.lbl1 = QLabel(self)
        self.lbl1.setText('Введите дату и время вылета в формате дд.мм.гггг:')
        self.lbl1.move(15, 10)
        self.field = QLineEdit(self)
        self.field.resize(150, 50)
        self.field.move(75, 30)
        self.lbl2 = QLabel(self)
        self.lbl2.move(75, 80)
        self.lbl2.resize(200, 30)
        self.btn1 = QPushButton('Далее', self)
        self.btn1.resize(150, 50)
        self.btn1.move(75, 110)
        self.btn1.clicked.connect(self.run1)
        self.btn2 = QPushButton('Назад', self)
        self.btn2.resize(150, 50)
        self.btn2.move(75, 180)
        self.btn2.clicked.connect(self.run2)

    def run1(self):
        pass

    def run2(self):
        self.close()
        self.window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainMenu()
    ex.show()
    sys.exit(app.exec())
