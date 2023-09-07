# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 640)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255,255,255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(24, 90, 119);\n"
"border: 1px solid rgb(24, 90, 119);\n"
"border-radius: 15px;")
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo = QtWidgets.QLabel(self.frame)
        self.logo.setMaximumSize(QtCore.QSize(50, 50))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/images/images/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.horizontalLayout.addWidget(self.logo)
        self.title = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Rostov")
        font.setPointSize(18)
        font.setKerning(True)
        self.title.setFont(font)
        self.title.setStyleSheet("font: 18pt \"Rostov\";\n"
"color: rgb(255, 255, 255)")
        self.title.setTextFormat(QtCore.Qt.PlainText)
        self.title.setObjectName("title")
        self.horizontalLayout.addWidget(self.title)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.slogan = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Hitmo2.0")
        font.setPointSize(9)
        font.setKerning(False)
        self.slogan.setFont(font)
        self.slogan.setStyleSheet("color: rgba(255, 255, 255, 180);\n"
"font: 9pt \"Hitmo2.0\";")
        self.slogan.setObjectName("slogan")
        self.horizontalLayout_3.addWidget(self.slogan)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.frame)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.task = QtWidgets.QFrame(self.centralwidget)
        self.task.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.task.setFrameShadow(QtWidgets.QFrame.Raised)
        self.task.setObjectName("task")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.task)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.combo = QtWidgets.QComboBox(self.task)
        font = QtGui.QFont()
        font.setFamily("Hitmo2.0")
        font.setPointSize(10)
        font.setKerning(False)
        self.combo.setFont(font)
        self.combo.setToolTip("")
        self.combo.setStatusTip("")
        self.combo.setStyleSheet("QComboBox {\n"
"    border: 1px groove gray;\n"
"    border-radius: 13px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    color: gray;\n"
"    background: rgb(240, 245, 247);\n"
"    font: 10pt \"Hitmo2.0\";\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-top-right-radius: 13px;\n"
"    border-bottom-right-radius: 13px;\n"
"}\n"
"")
        self.combo.setEditable(False)
        self.combo.setObjectName("combo")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.combo.addItem(icon1, "")
        self.combo.addItem(icon1, "")
        self.combo.addItem(icon1, "")
        self.combo.addItem(icon1, "")
        self.combo.addItem(icon1, "")
        self.combo.addItem(icon1, "")
        self.verticalLayout_3.addWidget(self.combo)
        self.tasklayout = QtWidgets.QGridLayout()
        self.tasklayout.setObjectName("tasklayout")
        self.verticalLayout_3.addLayout(self.tasklayout)
        self.horizontalLayout_4.addWidget(self.task)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.classic = QtWidgets.QFrame(self.centralwidget)
        self.classic.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.classic.setFrameShadow(QtWidgets.QFrame.Raised)
        self.classic.setObjectName("classic")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.classic)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.classictabtitle = QtWidgets.QLabel(self.classic)
        font = QtGui.QFont()
        font.setFamily("Hitmo2.0")
        font.setPointSize(12)
        font.setKerning(False)
        self.classictabtitle.setFont(font)
        self.classictabtitle.setStyleSheet("color: rgb(28, 28, 49);\n"
"font: 12pt \"Hitmo2.0\";")
        self.classictabtitle.setObjectName("classictabtitle")
        self.horizontalLayout_5.addWidget(self.classictabtitle)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.classicbtn = QtWidgets.QPushButton(self.classic)
        self.classicbtn.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Hitmo2.0")
        font.setPointSize(10)
        self.classicbtn.setFont(font)
        self.classicbtn.setStyleSheet("QPushButton{\n"
"border:2px groove rgb(24, 90, 119);\n"
"border-radius:15px;\n"
"padding:2px 4px;\n"
"background-color: rgb(24, 90, 119);\n"
"color:rgb(255,255,255);\n"
"font: 10pt \"Hitmo2.0\";\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"border:2px groove rgb(240, 245, 247);\n"
"background-color: rgb(240, 245, 247);\n"
"color: gray;\n"
"}")
        self.classicbtn.setObjectName("classicbtn")
        self.horizontalLayout_5.addWidget(self.classicbtn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.classiclayout = QtWidgets.QGridLayout()
        self.classiclayout.setObjectName("classiclayout")
        self.verticalLayout_5.addLayout(self.classiclayout)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.classic)
        self.quantum = QtWidgets.QFrame(self.centralwidget)
        self.quantum.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.quantum.setFrameShadow(QtWidgets.QFrame.Raised)
        self.quantum.setObjectName("quantum")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.quantum)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.quantumtabtitle = QtWidgets.QLabel(self.quantum)
        font = QtGui.QFont()
        font.setFamily("Hitmo2.0")
        font.setPointSize(12)
        font.setKerning(False)
        self.quantumtabtitle.setFont(font)
        self.quantumtabtitle.setStyleSheet("color: rgb(28, 28, 49);\n"
"font: 12pt \"Hitmo2.0\";")
        self.quantumtabtitle.setObjectName("quantumtabtitle")
        self.horizontalLayout_6.addWidget(self.quantumtabtitle)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.quantumbtn = QtWidgets.QPushButton(self.quantum)
        font = QtGui.QFont()
        font.setFamily("Hitmo2.0")
        font.setPointSize(10)
        self.quantumbtn.setFont(font)
        self.quantumbtn.setStyleSheet("QPushButton{\n"
"border:2px groove rgb(24, 90, 119);\n"
"border-radius:15px;\n"
"padding:2px 4px;\n"
"background-color: rgb(24, 90, 119);\n"
"color:rgb(255,255,255);\n"
"font: 10pt \"Hitmo2.0\";\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"border:2px groove rgb(240, 245, 247);\n"
"background-color: rgb(240, 245, 247);\n"
"color: gray;\n"
"}")
        self.quantumbtn.setObjectName("quantumbtn")
        self.horizontalLayout_6.addWidget(self.quantumbtn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.quantumlayout = QtWidgets.QGridLayout()
        self.quantumlayout.setObjectName("quantumlayout")
        self.verticalLayout_6.addLayout(self.quantumlayout)
        self.verticalLayout_6.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.quantum)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.setStretch(1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.combo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QPtion"))
        self.title.setText(_translate("MainWindow", "QPtion"))
        self.slogan.setText(_translate("MainWindow", "   Price your option using our latest quantum technology."))
        self.combo.setCurrentText(_translate("MainWindow", "European Call"))
        self.combo.setItemText(0, _translate("MainWindow", "European Call"))
        self.combo.setItemText(1, _translate("MainWindow", "European Put"))
        self.combo.setItemText(2, _translate("MainWindow", "American Call"))
        self.combo.setItemText(3, _translate("MainWindow", "American Put"))
        self.combo.setItemText(4, _translate("MainWindow", "Asian Call"))
        self.combo.setItemText(5, _translate("MainWindow", "Asian Put"))
        self.classictabtitle.setText(_translate("MainWindow", "Classic"))
        self.classicbtn.setText(_translate("MainWindow", " Run "))
        self.quantumtabtitle.setText(_translate("MainWindow", "Quantum"))
        self.quantumbtn.setText(_translate("MainWindow", " Run "))
import assets.assets_rc
