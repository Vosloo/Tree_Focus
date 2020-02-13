from PyQt5 import QtCore, QtGui, QtWidgets

class Tree(QtWidgets.QLabel):
    
    def __init__(self, central_widget):
        super().__init__(central_widget)
        self.central_widget = central_widget 

    def initialize(self):
        self.setGeometry(QtCore.QRect(0, 0, self.central_widget.size().width(), self.central_widget.size().height()))
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setPixmap(QtGui.QPixmap("imgs/stage_0.PNG"))
        self.setObjectName("tree")