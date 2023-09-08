import matplotlib
from PyQt5.QtCore import QThread, pyqtSignal
from qiskit import QuantumCircuit

from ui.EuropeanPut.quantum import Ui_quantumwidget
from utils import EuropeanPut

matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


from PyQt5.QtWidgets import QWidget, QSizePolicy, QPushButton

from ui.EuropeanPut.classic import Ui_classicwidget
from ui.EuropeanPut.task import Ui_taskwidget


class taskwidget(QWidget, Ui_taskwidget):
    def __init__(self):
        QWidget.__init__(self)
        Ui_taskwidget.__init__(self)
        self.setupUi(self)

    def get_data(self):
        s0 = float(self.stockprice.text())
        k = float(self.strikeprice.text())
        t = float(self.maturity.text())
        r = float(self.marketrate.text())
        sigma = float(self.volatility.text())
        eps = float(self.accuracy.text())
        return [s0, k, t, r, sigma, eps]

class classicwidget(QWidget, Ui_classicwidget):
    def __init__(self):
        QWidget.__init__(self)
        Ui_classicwidget.__init__(self)
        self.setupUi(self)
        self.figure = classicFigure()
        self.figurelayout.addWidget(self.figure)

    def run(self, param: list, btn: QPushButton):
        self.btn = btn
        n = int(self.simulations.text())
        thread = classicThread(self, param + [n])
        thread.finishSignal.connect(self.show_result)
        thread.start()

    def show_result(self, result: dict):
        self.btn.setEnabled(True)

class quantumwidget(QWidget, Ui_quantumwidget):
    def __init__(self):
        QWidget.__init__(self)
        Ui_quantumwidget.__init__(self)
        self.setupUi(self)
        self.figure = quantumFigure()
        self.figurelayout.addWidget(self.figure)

class classicFigure(FigureCanvas):
    def __init__(self):
        figure = Figure(tight_layout=True)
        self.axes = figure.add_subplot(111)
        FigureCanvas.__init__(self, figure)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.axes.set_xlabel("Samples")
        self.axes.set_ylabel("Price")
        FigureCanvas.updateGeometry(self)

class quantumFigure(FigureCanvas):
    def __init__(self):
        self.figure = QuantumCircuit(1, 0).draw("mpl", style="iqx")
        FigureCanvas.__init__(self, self.figure)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Fixed, QSizePolicy.Fixed)
        FigureCanvas.updateGeometry(self)

class classicThread(QThread):
    finishSignal = pyqtSignal(dict)

    def __init__(self, parent, param):
        QThread.__init__(self, parent)
        self.parma = param

    def run(self) -> None:
        self.finishSignal.emit(EuropeanPut.classic(self.parma))