import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMenu, QMenuBar, QStatusBar, QAction
    )
from Main_menu import MainMenu
from New_tree import Tree

menu_file_style = """
QMenuBar::item {
    spacing: 3px;
    padding: 2px 10px;
    background-color: rgb(180,213,78);
    color: black;
    border-radius: 5px;
}
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setup_window()
        self.create_menubar()
        self.start_main_menu()

    def setup_window(self, width=900, height=650):
        self.setWindowTitle("Focus")
        self.resize(width, height)
        self.setStyleSheet("background-color:rgb(239,234,150)")
        self._set_icon()

    def _set_icon(self):
        icon = QIcon()
        icon.addFile('imgs/tree_app_icon.png', QSize(512, 512))
        self.setWindowIcon(icon)

    def create_menubar(self):
        self.menubar = QMenuBar(self)

        self.menuFile = QMenu(self.menubar)
        self.menuFile.setTitle("File")
        self.menuFile.setStyleSheet("background-color:rgb(192,228,82);")

        self.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(self)

        self.setStatusBar(self.statusbar)

        self.action_new_tree = QAction(self)
        self.action_new_tree.setText("New focus")
        self.action_new_tree.setShortcut("Ctrl+N")
        self.action_new_tree.triggered.connect(self.new_tree)

        self.action_forest = QAction(self)
        self.action_forest.setText("Forest")
        self.action_forest.setShortcut("Ctrl+F")
        self.action_forest.triggered.connect(self.forest)

        self.action_exit = QAction(self)
        self.action_exit.setText("Exit")
        self.action_exit.setShortcut("Esc")
        self.action_exit.triggered.connect(self.exit_app)

        self.menuFile.addAction(self.action_new_tree)
        self.menuFile.addAction(self.action_forest)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_exit)

        self.menubar.addAction(self.menuFile.menuAction())

    def start_main_menu(self):
        self.main_menu = MainMenu(self)
        self.setCentralWidget(self.main_menu)

        self.main_menu.button_new_tree.clicked.connect(self.new_tree)
        self.main_menu.button_forest.clicked.connect(self.forest)
        self.main_menu.button_exit.clicked.connect(self.exit_app)

        self.show()

    def new_tree(self):
        self.tree = Tree(self)
        self.setCentralWidget(self.tree)

    def forest(self):
        print('Forest')

    def exit_app(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(menu_file_style)

    window = MainWindow()
    sys.exit(app.exec_())
