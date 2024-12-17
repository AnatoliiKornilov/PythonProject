import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

import TakingTicketPassenger


# окно, на котором будет выводиться вся база данных с учётом всех предыдущих вводов пользователя.
# Также оно будет запрашивать номер рейса, который выберет пользователь
class TakingTicketChooseFlight(QMainWindow):
    def __init__(self, window, start_city, finish_city, date, passengers_count):
        super().__init__()
        self.initUI()
        self.window = window
        self.start_city = start_city
        self.finish_city = finish_city
        self.date = date
        self.passengers_count = passengers_count
        self.activities()

    def initUI(self):
        self.setMinimumSize(400, 200)
        uic.loadUi('table1.ui', self)
        self.pushButton.clicked.connect(self.openTakingTicketPassenger)
        self.pushButton_2.clicked.connect(self.goToPreviousWindow)
        self.pushButton.setMaximumHeight(75)
        self.pushButton_2.setMaximumHeight(75)

    def activities(self):
        connect = sqlite3.connect('project.sqlite3')
        cursor = connect.cursor()
        self.result = cursor.execute("""SELECT * FROM aviareycy""").fetchall()
        self.elements = []
        for record in self.result:
            record = list(record)
            check = True
            if record[2] != self.start_city:
                check = False
            if record[3] != self.finish_city:
                check = False
            data = record[4].split()
            if data[0] != self.date:
                check = False
            if record[5] < self.passengers_count:
                check = False
            if check:
                self.elements.append(record)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(len(self.elements))
        self.tableWidget.setHorizontalHeaderLabels(["Номер рейса", "Авиакомпания",
                                                    "Пункт вылета", "Пункт \n назначения",
                                                    "Дата и время \n вылета",
                                                    "Количество \n свободных мест",
                                                    "Стоимость \n билета(руб)"])
        for record in range(len(self.elements)):
            for j in range(7):
                elem = self.elements[record][j]
                self.tableWidget.setItem(record, j, QTableWidgetItem(str(elem)))
        if len(self.elements) == 0:
            self.label_3.setText('К сожалению, подходящих для Вас рейсов нет')

    def openTakingTicketPassenger(self):
        text = self.lineEdit.text()
        ids = []
        for element in self.elements:
            ids.append(element[0])
        if not text.isdigit():
            self.label_3.setText('      Введите корректный номер рейса')
        elif int(text) not in ids:
            self.label_3.setText('      Введите корректный номер рейса')
        else:
            self.close()
            self.window1 = TakingTicketPassenger.TakingTicketPassenger(self, 1, self.passengers_count, text)
            self.window1.show()
            self.window1.act()

    def goToPreviousWindow(self):
        self.close()
        self.window.show()
