from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QWidget


class TakingTicketDatetime(QWidget):
    def __init__(self, window, start_city, finish_city):
        super().__init__()
        self.initUI()
        self.window = window
        self.start_city = start_city
        self.finish_city = finish_city

    def initUI(self):
        self.setGeometry(300, 300, 300, 250)
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
        self.btn1.clicked.connect(self.run1)
        self.btn2 = QPushButton('Назад', self)
        self.btn2.resize(150, 50)
        self.btn2.move(75, 180)
        self.btn2.clicked.connect(self.run2)

    def run1(self):
        pass

    def run2(self):
        self.close()
        self.window.show()
