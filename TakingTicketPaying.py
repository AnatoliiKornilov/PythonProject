import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

from TheEnd import TheEnd


# окно, на котором будет выводиться вся важная итоговая информация о рейсе и о пассажирах
# только после нажатия на кнопку подтвердить изменения сохранятся в баззе данных
# а именно на выбранный рейс уменьшится количество свободных мест
class TakingTicketPaying(QMainWindow):
    def __init__(self, window, passengers, flight):
        super().__init__()
        self.initUI()
        self.window = window
        self.passengers = passengers
        self.flight = flight

    def initUI(self):
        self.setMinimumSize(400, 200)
        uic.loadUi('table2.ui', self)
        self.pushButton.clicked.connect(self.openTheEnd)
        self.pushButton_2.clicked.connect(self.goToPreviousWindow)

    def act(self):
        connect = sqlite3.connect('project.sqlite3')
        cursor = connect.cursor()
        self.result = cursor.execute("""SELECT * FROM aviareycy""").fetchall()
        data = []
        for record in self.result:
            record = list(record)
            if record[0] == int(self.flight):
                data = record.copy()
                break
        flight = 'Номер рейса: ' + str(data[0])
        self.label_2.setText(flight)
        company = 'Авиакомпания: ' + data[1]
        self.label_3.setText(company)
        start = 'Пункт вылета: ' + data[2]
        self.label_4.setText(start)
        finish = 'Пункт назначения: ' + data[3]
        self.label_5.setText(finish)
        datetime = 'Дата и время вылета: ' + data[4]
        self.label_6.setText(datetime)
        price = 'Стоимость покупки: ' + str(data[6] * len(self.passengers))
        self.label_7.setText(price)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(len(self.passengers))
        self.tableWidget.setHorizontalHeaderLabels(["Фамилия", "Имя",
                                                    "Отчество", "Серия",
                                                    "Номер"])
        for i in range(len(self.passengers)):
            for j in range(5):
                passenger = self.passengers[i][j]
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(passenger)))

    def openTheEnd(self):
        connect = sqlite3.connect('project.sqlite3')
        cursor = connect.cursor()
        self.result = cursor.execute("""SELECT * FROM aviareycy WHERE ID = ?""", (self.flight,)).fetchall()
        amount_of_available_seats = self.result[0][5]
        amount_of_seats_left = amount_of_available_seats - len(self.passengers)
        cursor.execute("""UPDATE aviareycy SET Free_seats = ? WHERE ID = ?""", (amount_of_seats_left, self.flight))
        connect.commit()
        self.close()
        self.window1 = TheEnd()
        self.window1.show()

    def goToPreviousWindow(self):
        self.close()
        self.window.show()
        self.window.act()
