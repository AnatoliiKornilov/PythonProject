import sqlite3

from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QSizePolicy, QHBoxLayout

import TakingTicketDateTime
from constants import database, russian_alphabet


class TakingTicketFinishCity(QWidget):
    def __init__(self, window2, start_city):
        super().__init__()
        self.initUI()
        self.window = window2
        self.start_city = start_city

    def initUI(self):
        self.setMinimumSize(400, 200)
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
        self.btn1.clicked.connect(self.TakingTicketDateTime)
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

    # как и все кнопки далее данная функция проверяет корректность введённого пользователем,
    # сообщает о некорректности, если надо, или сохраняет данные и переводит на следующее окно
    def TakingTicketDateTime(self):
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        city = self.field.text()
        check = True
        for letter in city:
            if not (letter in russian_alphabet or letter == '-' or letter == ' '):
                check = False
                self.lbl1.setText('Такого пункта назначения нет, \n введите корректное название')
        if check:
            result = cursor.execute("""SELECT Finish FROM aviareycy""").fetchall()
            records = []
            for record in result:
                records.append(record[0])
            if city in records:
                self.finish_city = city
                self.close()
                self.window1 = TakingTicketDateTime.TakingTicketDateTime(self, self.start_city, self.finish_city)
                self.window1.show()
            else:
                self.lbl1.setText('Такого пункта назначения нет, \n введите корректное название')

    # стандартная функция кнопки назад
    def goToPreviousWindow(self):
        self.close()
        self.window.show()
