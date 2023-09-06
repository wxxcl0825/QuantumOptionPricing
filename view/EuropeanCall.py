from PyQt5.QtWidgets import QWidget

from ui.EuropeanCall.task import Ui_taskwidget
from ui.EuropeanCall.classic import Ui_classicwidget
from ui.EuropeanCall.quantum import Ui_quantumwidget

class taskwidget(QWidget ,Ui_taskwidget):
    def __init__(self):
        QWidget.__init__(self)
        Ui_taskwidget.__init__(self)
        self.setupUi(self)


class classicwidget(QWidget, Ui_classicwidget):
    def __init__(self):
        QWidget.__init__(self)
        Ui_classicwidget.__init__(self)
        self.setupUi(self)

class quantumwidget(QWidget, Ui_quantumwidget):
    def __init__(self):
        QWidget.__init__(self)
        Ui_quantumwidget.__init__(self)
        self.setupUi(self)