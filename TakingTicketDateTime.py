import sqlite3

from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QSizePolicy, QHBoxLayout

import TakingTicketPassengersCount
from constants import database


# класс для окна, которое будет принимать и анализировать дату вылета пользователя
class TakingTicketDateTime(QWidget):
    def __init__(self, window, start_city, finish_city):
        super().__init__()
        self.initUI()
        self.window = window
        self.start_city = start_city
        self.finish_city = finish_city

    def initUI(self):
        self.setMinimumSize(400, 200)
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
        self.btn1.clicked.connect(self.openTakingTicketPassengerCount)
        self.btn2 = QPushButton('Назад', self)
        self.btn2.resize(150, 50)
        self.btn2.move(75, 180)
        self.btn2.clicked.connect(self.goToPreviousWindow)
        self.btn1.setMaximumHeight(75)
        self.btn2.setMaximumHeight(75)

        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.lbl1)
        self.vbox.addWidget(self.field)
        self.vbox.addWidget(self.lbl2)
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

    def openTakingTicketPassengerCount(self):
        # стандартная функция кнопки далее
        date = str(self.field.text())
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        check = True
        for letter in date:
            if not (letter.isdigit() or letter == '.'):
                check = False
                self.lbl2.setText('Такой даты вылета нет, \n введите другую')
        if check:
            result = cursor.execute("""SELECT Date_time FROM aviareycy""").fetchall()
            dates = []
            for record in result:
                elem = record[0].split()
                dates.append(elem[0])
            if date not in dates:
                self.lbl2.setText('Такой даты вылета нет, \n введите другую')
            else:
                self.date = date
                self.close()
                self.window1 = TakingTicketPassengersCount.TakingTicketPassengersCount(self, self.start_city,
                                                                                       self.finish_city, self.date)
                self.window1.show()

    # стандартная функция кнопки назад
    def goToPreviousWindow(self):
        self.close()
        self.window.show()
