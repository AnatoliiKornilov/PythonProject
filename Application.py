import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy, \
    QWidget

import TakingTicketStartCity
from SeeDataBase import SeeDataBase
from constants import database

# подключим базу данных
connection = sqlite3.connect(database)
cursor = connection.cursor()


# создадим окно главного меню
class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setMinimumSize(400, 200)
        self.lbl = QLabel(self)
        self.lbl.setText('Выберите опцию:')
        self.btn1 = QPushButton('Забронировать билет', self)
        self.btn1.clicked.connect(self.openTakingTicketStartCity)
        self.btn2 = QPushButton('Посмотреть расписание', self)
        self.btn2.clicked.connect(self.openDatabaseWindow)
        self.btn1.setMaximumHeight(75)
        self.btn2.setMaximumHeight(75)

        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.lbl)
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

    # при помощи данной функции мы перейдём на первое окно бронирования билета
    def openTakingTicketStartCity(self):
        self.close()
        self.nextWindow = TakingTicketStartCity.TakingTicketStartCity(self)
        self.nextWindow.show()

    # данная функция переведёт нас к окну с расписания
    def openDatabaseWindow(self):
        self.close()
        self.windowDatabase = SeeDataBase(self)
        self.windowDatabase.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec())
