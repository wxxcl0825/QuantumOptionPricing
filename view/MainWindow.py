from PyQt5.QtWidgets import QMainWindow

from ui.MainWindow import Ui_MainWindow
from view import EuropeanCall


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # load subview
        self.taskwidget = EuropeanCall.taskwidget()
        self.tasklayout.addWidget(self.taskwidget)
        self.taskwidget.show()
        self.classicwidget = EuropeanCall.classicwidget()
        self.classiclayout.addWidget(self.classicwidget)
        self.classicwidget.show()
        self.quantumwidget = EuropeanCall.quantumwidget()
        self.quantumlayout.addWidget(self.quantumwidget)
        self.quantumwidget.show()