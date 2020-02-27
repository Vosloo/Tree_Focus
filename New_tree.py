from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPixmap


class Tree(QLabel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        self.initialize()

    def initialize(self):
        self.debug_butt = QPushButton('DEBUG', self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.debug_butt)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox)

        self.setLayout(hbox)

        self.setGeometry(QRect(  # TODO: add app logic duh
            0, 0, self.parent.size().width(), self.parent.size().height()
            ))
        self.setAlignment(Qt.AlignCenter)
        self.setPixmap(QPixmap("imgs/stage_0.PNG"))
        self.setObjectName("tree")
