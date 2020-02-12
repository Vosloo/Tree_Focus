from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi()

    def setupUi(self):

        self.setup_window()

        font = self.set_font()
        self.create_main_menu(font)
        self.create_menubar()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle(_translate("MainWindow", "Tree Focus"))

        self.button_new_tree.setText(_translate("MainWindow", "New Tree"))
        self.button_forest.setText(_translate("MainWindow", "Forest"))
        self.button_exit.setText(_translate("MainWindow", "Exit"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))

        self.action_new_tree.setText(_translate("MainWindow", "New Tree"))
        self.action_new_tree.setShortcut(_translate("MainWindow", "Ctrl+N"))

        self.action_forest.setText(_translate("MainWindow", "Forest"))
        self.action_forest.setShortcut(_translate("MainWindow", "Ctrl+F"))

        self.action_exit.setText(_translate("MainWindow", "Exit"))
        self.action_exit.setShortcut(_translate("MainWindow", "Esc"))

    def exit_app(self):
        QtWidgets.QApplication.exit()

    def forest(self):
        print('Forest')

    def new_tree(self):
        print('New tree')

    def set_font(self):
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        return font

    def create_main_menu(self, font):
        self.button_new_tree = QtWidgets.QPushButton(self.centralwidget)
        self.button_new_tree.setGeometry(QtCore.QRect(349, 120, 201, 61))
        self.button_new_tree.setFont(font)
        self.button_new_tree.setObjectName("button_new_tree")
        self.button_new_tree.clicked.connect(self.new_tree)

        self.button_forest = QtWidgets.QPushButton(self.centralwidget)
        self.button_forest.setGeometry(QtCore.QRect(349, 260, 201, 61))
        self.button_forest.setFont(font)
        self.button_forest.setObjectName("button_forest")
        self.button_forest.clicked.connect(self.forest)

        self.button_exit = QtWidgets.QPushButton(self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(349, 400, 201, 61))
        self.button_exit.setFont(font)
        self.button_exit.setObjectName("button_exit")
        self.button_exit.clicked.connect(self.exit_app)

    def create_menubar(self):
        self.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")

        self.setStatusBar(self.statusbar)

        self.action_new_tree = QtWidgets.QAction(self)
        self.action_new_tree.setObjectName("action_new_tree")
        self.action_new_tree.triggered.connect(self.new_tree)

        self.action_forest = QtWidgets.QAction(self)
        self.action_forest.setObjectName("action_forest")
        self.action_forest.triggered.connect(self.forest)

        self.action_exit = QtWidgets.QAction(self)
        self.action_exit.setObjectName("action_exit")
        self.action_exit.triggered.connect(self.exit_app)

        self.menuFile.addAction(self.action_new_tree)
        self.menuFile.addAction(self.action_forest)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_exit)

        self.menubar.addAction(self.menuFile.menuAction())

    def setup_window(self, width=900, height=650):

        self.setObjectName("MainWindow")
        self.resize(width, height)

        icon = QtGui.QIcon()
        icon.addFile('imgs/tree_app_icon.png', QtCore.QSize(512, 512))
        self.setWindowIcon(icon)

        # self.setStyleSheet("background-color:rgb(239,234,150)") #TODO: adjust background colors of menubar and buttons

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    ui = MainWindow()

    ui.show()
    sys.exit(app.exec_())