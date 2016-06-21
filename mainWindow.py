# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.12.dev1606101416
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 161, 551))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.btn_run = QtGui.QPushButton(self.groupBox)
        self.btn_run.setGeometry(QtCore.QRect(10, 20, 141, 31))
        self.btn_run.setObjectName(_fromUtf8("btn_run"))
        self.btn_reset_all = QtGui.QPushButton(self.groupBox)
        self.btn_reset_all.setGeometry(QtCore.QRect(10, 100, 141, 31))
        self.btn_reset_all.setObjectName(_fromUtf8("btn_reset_all"))
        self.btn_reset_sol = QtGui.QPushButton(self.groupBox)
        self.btn_reset_sol.setGeometry(QtCore.QRect(10, 140, 141, 31))
        self.btn_reset_sol.setObjectName(_fromUtf8("btn_reset_sol"))
        self.step_size = QtGui.QSpinBox(self.groupBox)
        self.step_size.setGeometry(QtCore.QRect(70, 270, 81, 22))
        self.step_size.setMaximum(10000000)
        self.step_size.setProperty("value", 100)
        self.step_size.setObjectName(_fromUtf8("step_size"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 270, 31, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.btn_run_next = QtGui.QPushButton(self.groupBox)
        self.btn_run_next.setGeometry(QtCore.QRect(10, 60, 141, 31))
        self.btn_run_next.setObjectName(_fromUtf8("btn_run_next"))
        self.step_max = QtGui.QSpinBox(self.groupBox)
        self.step_max.setGeometry(QtCore.QRect(70, 300, 81, 22))
        self.step_max.setMaximum(10000000)
        self.step_max.setProperty("value", 1000)
        self.step_max.setObjectName(_fromUtf8("step_max"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 330, 31, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tn = QtGui.QSpinBox(self.groupBox)
        self.tn.setGeometry(QtCore.QRect(70, 360, 81, 22))
        self.tn.setMaximum(1000)
        self.tn.setProperty("value", 0)
        self.tn.setObjectName(_fromUtf8("tn"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 360, 31, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.t0 = QtGui.QSpinBox(self.groupBox)
        self.t0.setGeometry(QtCore.QRect(70, 330, 81, 22))
        self.t0.setMaximum(1000)
        self.t0.setProperty("value", 20)
        self.t0.setObjectName(_fromUtf8("t0"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 300, 31, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.step_plot = QtGui.QSpinBox(self.groupBox)
        self.step_plot.setGeometry(QtCore.QRect(70, 240, 81, 22))
        self.step_plot.setMaximum(10000000)
        self.step_plot.setProperty("value", 10)
        self.step_plot.setObjectName(_fromUtf8("step_plot"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 51, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(180, 10, 301, 231))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.widget_objFunction = QtGui.QWidget(self.groupBox_2)
        self.widget_objFunction.setGeometry(QtCore.QRect(0, 20, 301, 211))
        self.widget_objFunction.setObjectName(_fromUtf8("widget_objFunction"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(180, 250, 611, 301))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.widget_graph = QtGui.QWidget(self.groupBox_4)
        self.widget_graph.setGeometry(QtCore.QRect(0, 20, 611, 281))
        self.widget_graph.setObjectName(_fromUtf8("widget_graph"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(490, 10, 301, 231))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.widget_temperature = QtGui.QWidget(self.groupBox_3)
        self.widget_temperature.setGeometry(QtCore.QRect(0, 20, 301, 211))
        self.widget_temperature.setObjectName(_fromUtf8("widget_temperature"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArquivo = QtGui.QMenu(self.menubar)
        self.menuArquivo.setObjectName(_fromUtf8("menuArquivo"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionStuff = QtGui.QAction(MainWindow)
        self.actionStuff.setObjectName(_fromUtf8("actionStuff"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuArquivo.addAction(self.actionStuff)
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.actionQuit)
        self.menubar.addAction(self.menuArquivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox", None))
        self.btn_run.setText(_translate("MainWindow", "Run Steps", None))
        self.btn_reset_all.setText(_translate("MainWindow", "Reset All", None))
        self.btn_reset_sol.setText(_translate("MainWindow", "Reset Solution", None))
        self.label.setText(_translate("MainWindow", "Step:", None))
        self.btn_run_next.setText(_translate("MainWindow", "Run util Improves", None))
        self.label_2.setText(_translate("MainWindow", "T_0:", None))
        self.label_3.setText(_translate("MainWindow", "T_n:", None))
        self.label_4.setText(_translate("MainWindow", "Max", None))
        self.label_5.setText(_translate("MainWindow", "PlotStep:", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Objective function", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Graph View", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Temperature", None))
        self.menuArquivo.setTitle(_translate("MainWindow", "File", None))
        self.actionStuff.setText(_translate("MainWindow", "Stuff", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))

