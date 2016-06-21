from PyQt4              import *
from mainWindow         import *
from drawingMachine     import *
from tsp                import *

import sys

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.actionQuit.triggered.connect(self.close)
        self.btn_run.clicked.connect(self.runTsp)
        self.btn_run_next.clicked.connect(self.runTspNext)
        self.btn_reset_sol.clicked.connect(self.resetSol)
        self.btn_reset_all.clicked.connect(self.resetAll)

        ################ DRAWING MAGIC ################
        self.widget_temperature = drawingMachine(self.widget_temperature)
        self.widget_temperature.setGeometry(QtCore.QRect(0, 0, 301, 211))
        self.widget_temperature.setObjectName("widget_temperature")
        self.widget_temperature.setIsTemp(True)
        self.widget_temperature.update()

        self.widget_objFunction = drawingMachine(self.widget_objFunction)
        self.widget_objFunction.setGeometry(QtCore.QRect(0, 0, 301, 211))
        self.widget_objFunction.setObjectName("widget_objFunction")
        self.widget_objFunction.setIsTemp(False)
        self.widget_objFunction.update()

        self.widget_graph = drawingMachine(self.widget_graph)
        self.widget_graph.setGeometry(QtCore.QRect(0, 0, 611, 281))
        self.widget_graph.setObjectName("widget_graph")
        self.widget_graph.update()
        ###############################################

        self.saEngine = simmulatedAnnealing()
        self.saEngine.setDrawer(self.widget_temperature, self.widget_objFunction)

        self.s0       = None
        self.sa_iter  = None

    def resetAll(self):
        self.widget_graph.clearClicked()
        self.resetSol()

    def resetSol(self):
        self.widget_graph.clearSol()
        self.s0      = None
        self.sa_iter = None
        self.widget_temperature.clearData()
        self.widget_objFunction.clearData()

    def runTsp(self):
        self.saEngine.updateConfig(self.t0.value(),
                                   self.tn.value(),
                                   self.step_max.value(),
                                   self.step_plot.value())

        self.s0, energy, self.sa_iter, T = self.saEngine.step(self.widget_graph.getClicked(), self.step_size.value(), self.s0, self.sa_iter)
        self.widget_graph.updateSol(self.s0)

    def runTspNext(self):
        self.saEngine.updateConfig(self.t0.value(),
                                   self.tn.value(),
                                   self.step_max.value(),
                                   self.step_plot.value())

        self.s0, energy, self.sa_iter, T = self.saEngine.step(self.widget_graph.getClicked(), self.step_size.value(), self.s0, self.sa_iter, True)
        self.widget_graph.updateSol(self.s0)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
