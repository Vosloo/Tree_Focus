from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import QRect


class MainMenu(QWidget):
    def __init__(self, font, parent=None):
        super(MainMenu, self).__init__(parent)
        self.font = font
        self.initialize()

    def _set_button_style(self):

        self.button_new_tree.setStyleSheet(
            "color:rgb(26, 26, 26);"
            "background-color:rgb(180,213,78);"
            "border-style: inset;"
            "border-width: 2px;"
            "border-radius: 20px;"
            "border-color: black;"
            )

        self.button_forest.setStyleSheet(
            "color:rgb(26, 26, 26);"
            "background-color:rgb(180,213,78);"
            "background-position:center;"
            "border-style: inset;"
            "border-width: 2px;"
            "border-radius: 20px;"
            "border-color: black;"
            )

        self.button_exit.setStyleSheet(
            "color:rgb(26, 26, 26);"
            "background-color:rgb(180,213,78);"
            "border-style: inset;"
            "border-width: 2px;"
            "border-radius: 20px;"
            "border-color: black;"
            )

    def initialize(self):
        self.button_new_tree = QPushButton(self)
        self.button_new_tree.setText("New focus")
        self.button_new_tree.setGeometry(QRect(349, 120, 201, 61))
        self.button_new_tree.setFont(self.font)

        self.button_forest = QPushButton(self)
        self.button_forest.setText("Forest")
        self.button_forest.setGeometry(QRect(349, 260, 201, 61))
        self.button_forest.setFont(self.font)

        self.button_exit = QPushButton(self)
        self.button_exit.setText("Exit")
        self.button_exit.setGeometry(QRect(349, 400, 201, 61))
        self.button_exit.setFont(self.font)

        self._set_button_style()
