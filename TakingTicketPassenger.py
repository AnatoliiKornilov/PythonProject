from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, QPushButton, QVBoxLayout, QSizePolicy, QHBoxLayout

import TakingTicketPaying


class TakingTicketPassenger(QWidget):
    def __init__(self, window, passenger_id, number_of_passengers, flight):
        super().__init__()
        self.initUI()
        self.window = window
        self.passengerId = passenger_id
        self.number_of_passengers = number_of_passengers
        self.passengers = []
        self.flight = flight

    def initUI(self):
        self.setMinimumSize(400, 200)
        self.lbl1 = QLabel(self)
        self.lbl1.move(50, 10)
        self.lbl1.setText('Введите паспортные данные пасажиров')
        self.lbl2 = QLabel(self)
        self.lbl2.resize(100, 20)
        self.lbl2.move(100, 30)
        self.lbl3 = QLabel(self)
        self.lbl3.move(10, 50)
        self.lbl3.setText('Фамилия:')
        self.field1 = QLineEdit(self)
        self.field1.resize(150, 30)
        self.field1.move(10, 70)
        self.lbl4 = QLabel(self)
        self.lbl4.move(10, 120)
        self.lbl4.setText('Имя:')
        self.field2 = QLineEdit(self)
        self.field2.resize(150, 30)
        self.field2.move(10, 140)
        self.lbl5 = QLabel(self)
        self.lbl5.move(10, 190)
        self.lbl5.setText('Отчество(- при отсутствии):')
        self.field3 = QLineEdit(self)
        self.field3.resize(150, 30)
        self.field3.move(10, 210)
        self.lbl6 = QLabel(self)
        self.lbl6.move(10, 260)
        self.lbl6.setText('Серия:')
        self.field4 = QLineEdit(self)
        self.field4.resize(150, 30)
        self.field4.move(10, 280)
        self.lbl7 = QLabel(self)
        self.lbl7.move(10, 330)
        self.lbl7.setText('Номер:')
        self.field5 = QLineEdit(self)
        self.field5.resize(150, 30)
        self.field5.move(10, 350)
        self.lbl8 = QLabel(self)
        self.lbl8.move(30, 400)
        self.lbl8.resize(250, 20)
        self.btn1 = QPushButton('Далее', self)
        self.btn1.resize(100, 30)
        self.btn1.move(100, 420)
        self.btn1.clicked.connect(self.openTakingTicketPayingOrPassenger)
        self.btn2 = QPushButton('Назад', self)
        self.btn2.resize(100, 30)
        self.btn2.move(100, 470)
        self.btn2.clicked.connect(self.goToPreviousWindow)
        self.btn1.setMaximumHeight(75)
        self.btn2.setMaximumHeight(75)
        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addWidget(self.lbl1)
        self.vbox.addWidget(self.lbl2)
        self.vbox.addWidget(self.lbl3)
        self.vbox.addWidget(self.field1)
        self.vbox.addWidget(self.lbl4)
        self.vbox.addWidget(self.field2)
        self.vbox.addWidget(self.lbl5)
        self.vbox.addWidget(self.field3)
        self.vbox.addWidget(self.lbl6)
        self.vbox.addWidget(self.field4)
        self.vbox.addWidget(self.lbl7)
        self.vbox.addWidget(self.field5)
        self.vbox.addWidget(self.lbl8)
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

    def act(self):
        passenger = 'Пассажир ' + str(self.passengerId)
        self.lbl2.setText(passenger)

    def openTakingTicketPayingOrPassenger(self):
        series = self.field4.text()
        check1 = True
        if len(series) != 4:
            check1 = False
        else:
            for i in range(len(series)):
                if not series[i].isdigit():
                    check1 = False
                    break
        number = self.field5.text()
        check2 = True
        if len(number) != 6:
            check2 = False
        else:
            for i in range(len(number)):
                if not number[i].isdigit():
                    check2 = False
                    break
        if not check1 and not check2:
            self.lbl8.setText('Серия и номер введены некорректно')
        elif not check1:
            self.lbl8.setText('Серия введена некорректно')
        elif not check2:
            self.lbl8.setText('Номер введён некорректно')
        elif self.field1.text() == '':
            self.lbl8.setText('Введите фамилию')
        elif self.field2.text() == '':
            self.lbl8.setText('Введите имя')
        elif self.field3.text() == '':
            self.lbl8.setText('Введите отчество')
        else:
            person = []
            person.append(self.field1.text())
            person.append(self.field2.text())
            person.append(self.field3.text())
            person.append(self.field4.text())
            person.append(self.field5.text())
            if len(self.passengers) < self.passengerId:
                self.passengers.append(person)
            else:
                self.passengers[self.passengerId - 1] = person
            if self.passengerId == self.number_of_passengers:
                self.close()
                self.window1 = TakingTicketPaying.TakingTicketPaying(self, self.passengers, self.flight)
                self.window1.show()
                self.window1.act()
            else:
                self.close()
                self.window1 = TakingTicketPassenger(self, self.passengerId + 1, self.number_of_passengers,
                                                     self.flight)
                self.window1.show()
                self.window1.act()

    def goToPreviousWindow(self):
        self.close()
        self.window.show()
