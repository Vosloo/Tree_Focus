from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QComboBox,
    QPushButton,
    QStyledItemDelegate
    )
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class AlignDelegate(QStyledItemDelegate):
    """Class for aligning items in combobox at center"""
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


class Tree(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        self.initialize()

    def initialize(self):
        self.create_layouts()
        self.create_query()

        self.time_box.activated.connect(self.time_box_option)
        self.ok_button.clicked.connect(
            lambda: self.start_focus(self.time_box.currentText())
        )

    def create_layouts(self):
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        self.hbox.addLayout(self.vbox)
        self.setLayout(self.hbox)

    def create_query(self):
        self.back_button = self.create_button("Back to menu")
        self.ok_button = self.create_button("Ok", font_size=14)
        self.query_label = self.create_query_label()
        self.time_box = self.create_time_box()

        self.vbox.addWidget(
            self.back_button, alignment=Qt.AlignTop | Qt.AlignLeft
        )

        self.vbox.addStretch()
        self.vbox.addWidget(self.query_label, alignment=Qt.AlignCenter)
        self.vbox.addSpacing(40)
        self.vbox.addWidget(self.time_box, alignment=Qt.AlignCenter)
        self.vbox.addSpacing(40)
        self.vbox.addWidget(self.ok_button, alignment=Qt.AlignCenter)
        self.vbox.addStretch()

    def create_button(self, name, font_size=10) -> QPushButton:
        button_style = (
            "color:rgb(26, 26, 26);"
            "background-color:rgb(180,213,78);"
            "width: 110px;"
            "height: 30px;"
            "border-style: inset;"
            "border-width: 2px;"
            "border-radius: 8px;"
            "border-color: black;"
        )

        button = QPushButton(
            name, self, font=self.set_font(size=font_size)
        )
        button.setStyleSheet(button_style)

        return button

    def create_query_label(self) -> QLabel:
        label_font = self.set_font(size=16, bold=False)

        label = QLabel(self)
        label.setText('How much time do You want to spend being focused?')
        label.setStyleSheet(
            "border-style: inset;"
            "border-radius: 10px;"
            "border-width: 2px;"
            "border-color: black;"
            "background-color: rgb(180,213,78)"
        )
        label.setFont(label_font)

        return label

    def create_time_box(self) -> QComboBox:
        items = ['15min', '30min', '1h', '2h', '4h', 'Custom: ']

        time_box_font = self.set_font(size=14)

        combo_box = QComboBox(self)
        combo_box.addItems(items)

        delegate = AlignDelegate(combo_box)
        combo_box.setItemDelegate(delegate)
        combo_box.setEditable(True)
        combo_box.lineEdit().setAlignment(Qt.AlignCenter)
        combo_box.lineEdit().setFont(time_box_font)
        combo_box.lineEdit().setReadOnly(True)
        combo_box.setFont(time_box_font)
        combo_box.setStyleSheet(
            "width: 200px;"
            "height: 50px;"
            "border-style: inset;"
            "border-width: 1px;"
            "border-color: black;"
        )

        return combo_box

    def time_box_option(self):
        if self.time_box.currentText() == 'Custom: ':
            self.time_box.lineEdit().setReadOnly(False)
            self.time_box.currentTextChanged.connect(self.input_custom)
        else:
            self.time_box.lineEdit().setReadOnly(True)

    # TODO: Prevent  adding another item to ComboBox after hitting Enter
    def input_custom(self):
        current_text = self.time_box.currentText()
        if current_text[:8] != 'Custom: ':
            self.time_box.setCurrentText('Custom: ' + current_text[7:])

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
