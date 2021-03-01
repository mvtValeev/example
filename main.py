import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False
        self.x, self.y = 100, 100

    def run(self):
        self.paint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()

    def draw_ellipse(self, qp):
        qp.setBrush(Qt.yellow)
        n = randint(1, 200)
        qp.drawEllipse(self.x, self.y, n, n)

    def paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
