from PyQt5 import QtCore, QtGui, QtWidgets
from New_tree import *
import sys

menu_file_style = """
QMenuBar::item {
    spacing: 3px;           
    padding: 2px 10px;
    background-color: rgb(180,213,78);
    color: black;  
    border-radius: 5px;
}
"""

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi()

    def setupUi(self):

        self.setup_window()

        self.font = self._set_font()

        self.create_main_menu()
        self.create_menubar()

        self.tree = Tree(self) #TODO: File menubar doesnt work, fix it

        self.connect_widgets()

    def connect_widgets(self):

        QtCore.QMetaObject.connectSlotsByName(self)

    def exit_app(self):
        self.close()

    def forest(self):
        print('Forest')

    def new_tree(self):
        print('New tree')
        self.toogle_main_menu()

        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.show()
        self.label.setGeometry(QtCore.QRect(0, 0, self.size().width(), self.size().height()))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setPixmap(QtGui.QPixmap("imgs/stage_6.PNG"))
        self.label.setObjectName("label")
        # self.tree.initialize()

        self.connect_widgets()

    def _set_font(self):
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        return font

    def _set_button_style(self):

        self.button_new_tree.setStyleSheet(
            "color:rgb(26, 26, 26);" 
            "background-color:rgb(180,213,78);" 
            "border-style: inset;" 
            "border-width: 2px;" 
            "border-radius: 20px;" 
            "border-color: black;")

        self.button_forest.setStyleSheet(
            "color:rgb(26, 26, 26);" 
            "background-color:rgb(180,213,78);" 
            "border-style: inset;" 
            "border-width: 2px;" 
            "border-radius: 20px;" 
            "border-color: black;")

        self.button_exit.setStyleSheet(
            "color:rgb(26, 26, 26);" 
            "background-color:rgb(180,213,78);" 
            "border-style: inset;" 
            "border-width: 2px;" 
            "border-radius: 20px;" 
            "border-color: black;")

    def create_main_menu(self):
        self.button_new_tree = QtWidgets.QPushButton(self.central_widget)
        self.button_new_tree.setText("New focus")
        self.button_new_tree.setGeometry(QtCore.QRect(349, 120, 201, 61))
        self.button_new_tree.setFont(self.font)
        self.button_new_tree.setObjectName("button_new_tree")
        self.button_new_tree.clicked.connect(self.new_tree)

        self.button_forest = QtWidgets.QPushButton(self.central_widget)
        self.button_forest.setText("Forest")
        self.button_forest.setGeometry(QtCore.QRect(349, 260, 201, 61))
        self.button_forest.setFont(self.font)
        self.button_forest.setObjectName("button_forest")
        self.button_forest.clicked.connect(self.forest)

        self.button_exit = QtWidgets.QPushButton(self.central_widget)
        self.button_exit.setText("Exit")
        self.button_exit.setGeometry(QtCore.QRect(349, 400, 201, 61))
        self.button_exit.setFont(self.font)
        self.button_exit.setObjectName("button_exit")
        self.button_exit.clicked.connect(self.exit_app)

        self._set_button_style()

    def create_menubar(self):
        self.setCentralWidget(self.central_widget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setTitle("File")
        self.menuFile.setObjectName("menuFile")
        self.menuFile.setStyleSheet("background-color:rgb(192,228,82);")

        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")

        self.setStatusBar(self.statusbar)

        self.action_new_tree = QtWidgets.QAction(self)
        self.action_new_tree.setText("New focus")
        self.action_new_tree.setShortcut("Ctrl+N")
        self.action_new_tree.setObjectName("action_new_tree")
        self.action_new_tree.triggered.connect(self.new_tree)

        self.action_forest = QtWidgets.QAction(self)
        self.action_forest.setText("Forest")
        self.action_forest.setShortcut("Ctrl+F")
        self.action_forest.setObjectName("action_forest")
        self.action_forest.triggered.connect(self.forest)

        self.action_exit = QtWidgets.QAction(self)
        self.action_exit.setText("Exit")
        self.action_exit.setShortcut("Esc")
        self.action_exit.setObjectName("action_exit")
        self.action_exit.triggered.connect(self.exit_app)

        self.menuFile.addAction(self.action_new_tree)
        self.menuFile.addAction(self.action_forest)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_exit)

        self.menubar.addAction(self.menuFile.menuAction())

    def setup_window(self, width=900, height=650):

        self.setObjectName("MainWindow")
        self.setWindowTitle("Focus")
        self.resize(width, height)

        icon = QtGui.QIcon()
        icon.addFile('imgs/tree_app_icon.png', QtCore.QSize(512, 512))
        self.setWindowIcon(icon)

        self.setStyleSheet("background-color:rgb(239,234,150)")

        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("central_widget")

    def toogle_main_menu(self):
        if self.button_new_tree.isVisible():
            self.button_new_tree.close()
            self.button_forest.close()
            self.button_exit.close()
        else:
            self.button_new_tree.show()
            self.button_forest.show()
            self.button_exit.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(menu_file_style)

    ui = MainWindow()

    ui.show()
    sys.exit(app.exec_())