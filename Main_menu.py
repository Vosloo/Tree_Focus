from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class MainMenu(QWidget):
    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)
        self.initialize()

    def _set_button_style(self):
        self.button_new_tree.setStyleSheet(self.style_sheet)
        self.button_forest.setStyleSheet(self.style_sheet)
        self.button_exit.setStyleSheet(self.style_sheet)

    def _set_style_sheet(self):
        self.style_sheet = (
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
        font.setPointSize(18)
        font.setBold(True)
        self.font = font

    def initialize(self):
        self._set_font()
        self._set_style_sheet()

        self.button_new_tree = QPushButton("New focus", self, font=self.font)
        self.button_forest = QPushButton("Forest", self, font=self.font)
        self.button_exit = QPushButton("Exit", self, font=self.font)

        self._set_button_style()

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(self.button_new_tree, alignment=Qt.AlignCenter)
        vbox.addSpacing(60)
        vbox.addWidget(self.button_forest, alignment=Qt.AlignCenter)
        vbox.addSpacing(60)
        vbox.addWidget(self.button_exit, alignment=Qt.AlignCenter)
        vbox.addStretch()

        hbox = QHBoxLayout()
        hbox.addLayout(vbox)

        self.setLayout(hbox)
