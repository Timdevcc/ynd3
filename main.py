import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from PyQt5 import uic


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dopaint = False
        uic.loadUi("gui.ui", self)
        self.pushButton.clicked.connect(self.do)

    def do(self):
        self.dopaint = True
        self.update()

    def paintEvent(self, event):
        if self.dopaint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 130, 130))
        x = random.randint(100, 200)
        qp.drawEllipse(30, 30, x, x)
        qp.drawEllipse(300, 30, x, x)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())