from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QMainWindow

from ui.MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.load_fonts()
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def load_fonts(self):
        QFontDatabase().addApplicationFont(":fonts/fonts/hitmo.ttf")
        QFontDatabase().addApplicationFont(":fonts/fonts/rostov.ttf")