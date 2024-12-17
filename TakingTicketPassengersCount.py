from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QSizePolicy, QHBoxLayout

import TakingTicketChooseFlight


class TakingTicketPassengersCount(QWidget):
    def __init__(self, window, start_city, finish_city, date):
        super().__init__()
        self.initUI()
        self.window = window
        self.start_city = start_city
        self.finish_city = finish_city
        self.date = date

    def initUI(self):
        self.setMinimumSize(400, 200)
        self.lbl1 = QLabel(self)
        self.lbl1.setText('Введите количество билетов:')
        self.lbl1.move(75, 10)
        self.field = QLineEdit(self)
        self.field.resize(150, 50)
        self.field.move(75, 30)
        self.lbl2 = QLabel(self)
        self.lbl2.move(75, 80)
        self.lbl2.resize(200, 30)
        self.btn1 = QPushButton('Далее', self)
        self.btn1.resize(150, 50)
        self.btn1.move(75, 110)
        self.btn1.clicked.connect(self.openTakingTicketChooseFlight)
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

    def openTakingTicketChooseFlight(self):
        passengers_count_str = str(self.field.text())
        if not passengers_count_str.isdigit():
            self.lbl2.setText('Введите корректное число пассажиров')
        elif int(passengers_count_str) <= 0:
            self.lbl2.setText('Введите корректное число пассажиров')
        else:
            self.passengers_count = int(passengers_count_str)
            self.close()
            self.window1 = TakingTicketChooseFlight.TakingTicketChooseFlight(self, self.start_city, self.finish_city,
                                                                             self.date, self.passengers_count)
            self.window1.show()

    def goToPreviousWindow(self):
        self.close()
        self.window.show()
