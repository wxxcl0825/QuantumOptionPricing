from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from ui.MainWindow import Ui_MainWindow
from view import EuropeanCall, EuropeanPut


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.load_europeancall()
        self.table = {
            "European Call": self.load_europeancall,
            "European Put": self.load_europeanput
        }
        self.combo.activated[str].connect(self.switch_option)


    @pyqtSlot()
    def on_classicbtn_clicked(self):
        self.classicbtn.setDisabled(True)
        self.classicwidget.run(self.taskwidget.get_data(), self.classicbtn)

    @pyqtSlot()
    def on_quantumbtn_clicked(self):
        self.quantumbtn.setDisabled(True)
        self.quantumwidget.run(self.taskwidget.get_data(), self.quantumbtn)

    def switch_option(self, text):
        self.taskwidget.close()
        self.classicwidget.close()
        self.quantumwidget.close()
        self.table[text]()


    def load_europeancall(self):
        self.taskwidget = EuropeanCall.taskwidget()
        self.tasklayout.addWidget(self.taskwidget)
        self.taskwidget.show()
        self.classicwidget = EuropeanCall.classicwidget()
        self.classiclayout.addWidget(self.classicwidget)
        self.classicwidget.show()
        self.quantumwidget = EuropeanCall.quantumwidget()
        self.quantumlayout.addWidget(self.quantumwidget)
        self.quantumwidget.show()

    def load_europeanput(self):
        self.taskwidget = EuropeanPut.taskwidget()
        self.tasklayout.addWidget(self.taskwidget)
        self.taskwidget.show()
        self.classicwidget = EuropeanPut.classicwidget()
        self.classiclayout.addWidget(self.classicwidget)
        self.classicwidget.show()
        self.quantumwidget = EuropeanPut.quantumwidget()
        self.quantumlayout.addWidget(self.quantumwidget)
        self.quantumwidget.show()
