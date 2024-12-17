import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from constants import database

# класс для открытия окна с полным расписанием всех рейсов
class SeeDataBase(QMainWindow):
    def __init__(self, window):
        super().__init__()
        self.initUI()
        self.window = window

    def initUI(self):
        self.setMinimumSize(500, 200)
        uic.loadUi('table.ui', self)
        self.pushButton.clicked.connect(self.openMainWindow)
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        result = cursor.execute("""SELECT * FROM aviareycy""").fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setHorizontalHeaderLabels(["Номер рейса", "Авиакомпания",
                                                    "Пункт вылета", "Пункт \n назначения",
                                                    "Дата и время \n вылета",
                                                    "Количество \n свободных мест",
                                                    "Стоимость \n билета(руб)"])
        elements = []
        for i in result:
            i = list(i)
            elements.append(i)
        for i in range(len(elements)):
            for j in range(7):
                elem = elements[i][j]
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

    def openMainWindow(self):
        # данная функция закроет текущее окно и откроет главное меню
        self.close()
        self.window.show()