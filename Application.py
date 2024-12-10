import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow

database = 'project.sqlite3'
connection = sqlite3.connect(database)
cursor = connection.cursor()


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
        self.btn1.clicked.connect(self.startTicket)
        self.btn2 = QPushButton('Посмотреть расписание', self)
        self.btn2.resize(150, 50)
        self.btn2.move(75, 125)
        self.btn2.clicked.connect(self.showSchedule)

    # функция для перехода на первое окно бронирования билета
    def startTicket(self):
        pass

    # функция для перехода в окно с расписанием
    def showSchedule(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainMenu()
    ex.show()
    sys.exit(app.exec())