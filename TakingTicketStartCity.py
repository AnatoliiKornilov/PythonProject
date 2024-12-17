import sqlite3

from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, QPushButton, QVBoxLayout, QSizePolicy, QHBoxLayout

import TakingTicketFinishCity
from constants import database, russian_alphabet


class TakingTicketStartCity(QWidget):
    def __init__(self, window1):
        super().__init__()
        self.initUI()
        self.window = window1

    def initUI(self):
        self.setMinimumSize(400, 200)
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
        self.btn1.clicked.connect(self.openTakingTicketFinishCity)
        self.btn2 = QPushButton('Назад', self)
        self.btn2.resize(150, 50)
        self.btn2.move(75, 180)
        self.btn2.clicked.connect(self.goToPreviousWindow)
        self.btn1.setMaximumHeight(75)
        self.btn2.setMaximumHeight(75)
        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.lbl)
        self.vbox.addWidget(self.field)
        self.vbox.addWidget(self.lbl1)
        self.vbox.addWidget(self.btn1)
        self.vbox.addWidget(self.btn2)
        self.vbox.addStretch(1)

        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addLayout(self.vbox)
        self.hbox.addStretch(1)

        self.setLayout(self.hbox)

        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(1)
        size_policy.setVerticalStretch(1)
        self.btn1.setSizePolicy(size_policy)
        self.btn2.setSizePolicy(size_policy)

    def openTakingTicketFinishCity(self):
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        text = self.field.text()
        check = True
        for letter in text:
            if not (letter in russian_alphabet or letter == '-' or letter == ' '):
                check = False
                self.lbl1.setText('Такого пункта вылета нет, \n введите корректное название')
        if check:
            result = cursor.execute("""SELECT Start FROM aviareycy""").fetchall()
            records = []
            for record in result:
                records.append(record[0])
            if text in records:
                self.start_city = text
                self.close()
                self.window1 = TakingTicketFinishCity.TakingTicketFinishCity(self, self.start_city)
                self.window1.show()
            else:
                self.lbl1.setText('Такого пункта вылета нет, \n введите корректное название')

    # эта функция работает как и все остальные кнопки назад, а именно закрывает текущее окно
    # и открывает старое
    def goToPreviousWindow(self):
        self.close()
        self.window.show()
