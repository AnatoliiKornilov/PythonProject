import sqlite3

from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
import TakingTicketDatetime

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

    def run1(self, database):
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        value = self.field.text()
        self.finish_city = value
        self.close()
        self.ex1 = TakingTicketDatetime.TakingTicketDatetime(self, self.start_city, self.finish_city)
        self.ex1.show()

    def run2(self):
        self.close()
        self.window.show()
