from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class MainMenu(QWidget):
    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)
        self.initialize()

    def _set_button_style(self):
        self.button_new_tree.setStyleSheet(
            "color:rgb(26, 26, 26);"
            "background-color:rgb(180,213,78);"
            "width: 201px;"
            "height: 61px;"
            "border-style: solid;"
            "border-width: 2px;"
            "border-radius: 20px;"
            "border-color: black;"
            )

        self.button_forest.setStyleSheet(
            "color:rgb(26, 26, 26);"
            "background-color:rgb(180,213,78);"
            "width: 201px;"
            "height: 61px;"
            "border-style: inset;"
            "border-width: 2px;"
            "border-radius: 20px;"
            "border-color: black;"
            )

        self.button_exit.setStyleSheet(
            "color:rgb(26, 26, 26);"
            "background-color:rgb(180,213,78);"
            "width: 201px;"
            "height: 61px;"
            "border-style: inset;"
            "border-width: 2px;"
            "border-radius: 20px;"
            "border-color: black;"
            )

    def _set_font(self):
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.font = font

    def initialize(self):
        self._set_font()

        self.button_new_tree = QPushButton("New focus", self, font=self.font)
        self.button_forest = QPushButton("Forest", self, font=self.font)
        self.button_exit = QPushButton("Exit", self, font=self.font)

        self._set_button_style()

        vbox = QVBoxLayout()
        vbox.addWidget(self.button_new_tree, alignment=Qt.AlignCenter)
        vbox.addWidget(self.button_forest, alignment=Qt.AlignCenter)
        vbox.addWidget(self.button_exit, alignment=Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox)

        self.setLayout(hbox)
