from PyQt5.QtWidgets import (
    QWidget,
    QMessageBox,
    QHBoxLayout,
    QVBoxLayout
    )
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from Query import Query
from Tree_timer import TimeArgException, TreeTimer


class Tree(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        self.query = Query(self)
        self.tree_timer = TreeTimer(self)

        self.initialize()

    def initialize(self):
        self.create_layouts()
        self.add_query_to_layout()

    def create_layouts(self):
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        self.hbox.addLayout(self.vbox)
        self.setLayout(self.hbox)

    def add_query_to_layout(self):

        self.vbox.addWidget(
            self.query.back_button, alignment=Qt.AlignTop | Qt.AlignLeft
        )

        self.vbox.addWidget(
            self.tree_timer, alignment=Qt.AlignTop | Qt.AlignRight
        )

        self.vbox.addStretch()
        self.vbox.addWidget(self.query.label, alignment=Qt.AlignCenter)
        self.vbox.addSpacing(40)
        self.vbox.addWidget(self.query, alignment=Qt.AlignCenter)
        self.vbox.addSpacing(40)
        self.vbox.addWidget(self.query.ok_button, alignment=Qt.AlignCenter)
        self.vbox.addStretch()

    def back_to_menu(self):
        """Switches back to main menu screen.
            It is called by Query after back button is activated."""

        self.parent.start_main_menu()

    # TODO: Implement tree growing logic
    def start_focus(self, time):
        try:
            self.tree_timer.initialize(time)
        except TimeArgException:
            invalid_message = "Invalid custom time!" + \
                "\nPossible inputs: [value] [m, min, h]"

            invalid_input = self.create_warning(invalid_message)
            invalid_input.exec()

    def create_warning(self, text) -> QMessageBox:
        """Creates pop-up warning window with set text"""
        warning = QMessageBox()
        warning.setIcon(QMessageBox.Warning)
        warning.setWindowTitle("Warning!")
        warning.setText(text)

        return warning

    # def resizeEvent(self, event):
    #     if self.tree_visible:
    #         self.tree.close()
    #         pixmap = QPixmap("imgs/stage_7.PNG").scaled(
    #             self.parent.width(),
    #             self.parent.height(),
    #             aspectRatioMode=Qt.KeepAspectRatio
    #             )
    #         self.tree.setPixmap(pixmap)
    #         self.tree.resize(self.parent.width(), self.parent.height())
    #         self.tree.show()

    def set_font(self, name="Arial", size=14, bold=True):
        font = QFont()
        font.setFamily(name)
        font.setPointSize(size)
        font.setBold(bold)

        return font
