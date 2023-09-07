import time

import matplotlib
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal
from qiskit import *

matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt5.QtWidgets import QWidget, QSizePolicy, QPushButton

from ui.EuropeanCall.task import Ui_taskwidget
from ui.EuropeanCall.classic import Ui_classicwidget
from ui.EuropeanCall.quantum import Ui_quantumwidget
from utils import EuropeanCall


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
        eps = result["eps"]
        bias = (result["result"] - result["BSM"]) / result["BSM"]
        self.result.setText(str(np.round(result["result"], eps)))
        self.bsm.setText(str(np.round(result["BSM"], eps)))
        self.bias.setText(f"{np.abs(bias) * 100:.2f}%")
        self.figure.plot(result["log"][0], result["log"][1], result["BSM"])
        self.btn.setEnabled(True)


class quantumwidget(QWidget, Ui_quantumwidget):
    def __init__(self):
        QWidget.__init__(self)
        Ui_quantumwidget.__init__(self)
        self.setupUi(self)
        self.figure = quantumFigure()
        self.figurelayout.addWidget(self.figure)

    def run(self, param: list, btn: QPushButton):
        self.btn = btn
        nbits = int(self.nbits.text())
        opt = int(self.optimizer.text())
        thread = quantumThread(self, param + [nbits, opt])
        thread.finishSignal.connect(self.show_result)
        thread.start()

    def show_result(self, result: dict):
        self.result.setText(f"{result['result']:.4f}")
        self.figure.plot(result["circuit"])
        self.btn.setEnabled(True)


class classicFigure(FigureCanvas):
    def __init__(self):
        figure = Figure(tight_layout=True)
        self.axes = figure.add_subplot(111)
        FigureCanvas.__init__(self, figure)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.axes.set_xlabel("Samples")
        self.axes.set_ylabel("Price")
        FigureCanvas.updateGeometry(self)

    def plot(self, x, y, baseline):
        self.axes.cla()
        self.axes.plot(x, y, color="#185a77")
        self.axes.axhline(baseline, color="#f0f5f7", linestyle="dashed")
        self.axes.set_xlabel("Samples")
        self.axes.set_ylabel("Price")
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()


class quantumFigure(FigureCanvas):
    def __init__(self):
        self.figure = QuantumCircuit(1, 0).draw("mpl", style="iqx")
        FigureCanvas.__init__(self, self.figure)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Fixed, QSizePolicy.Fixed)
        FigureCanvas.updateGeometry(self)

    def plot(self, circuit: QuantumCircuit):
        self.figure = circuit.draw("mpl", style="iqx", fold=-1)
        FigureCanvas.updateGeometry(self)



class classicThread(QThread):
    finishSignal = pyqtSignal(dict)

    def __init__(self, parent, param):
        QThread.__init__(self, parent)
        self.parma = param

    def run(self) -> None:
        self.finishSignal.emit(EuropeanCall.classic(self.parma))

class quantumThread(QThread):
    finishSignal = pyqtSignal(dict)
    def __init__(self, parent, param):
        QThread.__init__(self, parent)
        self.param = param

    def run(self) -> None:
        self.finishSignal.emit(EuropeanCall.quantum(self.param))