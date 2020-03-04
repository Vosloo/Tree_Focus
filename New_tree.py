from PyQt5.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout
    )
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from Query import Query


class Tree(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        self.query = Query(self)

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

        self.vbox.addStretch()
        self.vbox.addWidget(self.query.label, alignment=Qt.AlignCenter)
        self.vbox.addSpacing(40)
        self.vbox.addWidget(self.query, alignment=Qt.AlignCenter)
        self.vbox.addSpacing(40)
        self.vbox.addWidget(self.query.ok_button, alignment=Qt.AlignCenter)
        self.vbox.addStretch()

    def query_option(self):
        if self.query.currentIndex() == self.query.items_count - 1:
            self.query.lineEdit().setReadOnly(False)
            self.query.currentTextChanged.connect(self.input_custom)
        else:
            self.query.lineEdit().setReadOnly(True)

    def input_custom(self):
        current_text = self.query.currentText()
        if (self.query.currentIndex() == self.query.items_count - 1 and
                current_text[:8] != 'Custom: '):
            self.query.setCurrentText('Custom: ' + current_text[7:])

    # TODO: Implement tree growing logic
    def start_focus(self, time):
        print(time)

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
