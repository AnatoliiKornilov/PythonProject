from PyQt5.QtWidgets import QLabel, QPushButton, QWidget

import Application


# bill
class TheEnd(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.resize(700, 400)
        self.lbl.move(50, 10)
        self.lbl.setText('                       Ваш заказ успешно забронирован. \n \
                    Получить и оплатить билеты можно на кассе в аэропорту города, \n \
                    который Вы указали как пункт вылета. \n \
                    Наличие паспортов обязательно')
        self.btn = QPushButton('Вернуться в главное меню', self)
        self.btn.resize(200, 50)
        self.btn.move(175, 225)
        self.btn.clicked.connect(self.openMainWindow)

    def openMainWindow(self):
        self.close()
        self.window = Application.MainMenu()
        self.window.show()
