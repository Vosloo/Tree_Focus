from PyQt5.QtWidgets import QComboBox, QStyledItemDelegate, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class AlignDelegate(QStyledItemDelegate):
    """Class for aligning items in combobox at center"""
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


class Query(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.initialize_label()
        self.initialize_time_box()
        self.initialize_buttons()

        self.initialize_connections()

        self.setFocus()

    def set_font(self, name="Arial", size=14, bold=True) -> QFont:
        font = QFont()
        font.setFamily(name)
        font.setPointSize(size)
        font.setBold(bold)

        return font

    def initialize_label(self):
        """Initializes query label"""
        label_font = self.set_font(size=16, bold=False)

        self.label = QLabel(self)
        self.label.setText('How much time do You want to spend being focused?')
        self.label.setFixedHeight(50)
        self.label.setStyleSheet(
            "border-style: inset;"
            "border-radius: 10px;"
            "border-width: 1px;"
            "border-color: black;"
            "background-color: rgb(180,213,78)"
        )
        self.label.setFont(label_font)

    def initialize_time_box(self):
        """Initializes query ComboBox"""
        # Keep custom at the end of the list!
        self.custom_text = 'Custom: '
        items = ['15min', '30min', '1h', '2h', '4h', self.custom_text]
        self.items_count = len(items)

        time_box_font = self.set_font(size=14)

        self.addItems(items)

        delegate = AlignDelegate(self)
        self.setItemDelegate(delegate)
        self.setEditable(True)
        self.lineEdit().setAlignment(Qt.AlignCenter)
        self.lineEdit().setFont(time_box_font)
        self.lineEdit().setReadOnly(True)
        self.setFont(time_box_font)
        self.setStyleSheet(
            "width: 200px;"
            "height: 50px;"
            "border-style: inset;"
            "border-width: 1px;"
            "border-color: black;"
        )

    def initialize_buttons(self):
        """Initializes query buttons"""
        self.back_button = self.create_button("Back to menu")
        self.ok_button = self.create_button("Ok", font_size=14)

    def create_button(self, name, font_size=10) -> QPushButton:
        button_style = (
            "color:rgb(26, 26, 26);"
            "background-color:rgb(180,213,78);"
            "width: 110px;"
            "height: 30px;"
            "border-style: inset;"
            "border-width: 1px;"
            "border-radius: 8px;"
            "border-color: black;"
        )

        button = QPushButton(
            name, self, font=self.set_font(size=font_size)
        )
        button.setStyleSheet(button_style)

        return button

    def initialize_connections(self):
        """Initializes connections on event odccurance"""
        self.activated.connect(self.item_changed)
        self.currentTextChanged.connect(self.input_custom)

        self.ok_button.clicked.connect(self.activate_tree)
        self.back_button.clicked.connect(self.back_to_menu)

    def item_changed(self):
        """Called on event - combobox item changed"""
        if self.currentIndex() == self.items_count - 1:
            self.lineEdit().setReadOnly(False)
        else:
            self.lineEdit().setReadOnly(True)

    def input_custom(self):
        """Input custom option in time box"""
        current_text = self.currentText()
        if (self.currentIndex() == self.items_count - 1 and
                current_text[:len(self.custom_text)] != self.custom_text):

            if ':' in current_text:
                splitted_text = current_text.split(':')
            elif current_text == 'Custom ':
                splitted_text = current_text.split(' ')
            else:
                splitted_text = current_text.split()
            self.setCurrentText(self.custom_text + splitted_text[1].strip())

    def activate_tree(self):
        self.parent.start_focus(self.currentText())

    def back_to_menu(self):
        self.parent.back_to_menu()

    def keyPressEvent(self, key_event):
        if key_event.key() == Qt.Key_Return:
            self.ok_button.click()
        elif (key_event.key() == Qt.Key_Backspace and
                self.currentIndex() != self.items_count - 1):
            self.back_button.click()
        else:
            super().keyPressEvent(key_event)
