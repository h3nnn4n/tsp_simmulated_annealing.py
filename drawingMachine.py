from PyQt4              import *

class drawingMachine(QtGui.QWidget):
    def __init__(self, parent = None):
        super(drawingMachine, self).__init__(parent)
        self.mapMagic = None
        self.clicked  = set()
        self.sol      = None

    def getClicked(self):
        return list(self.clicked)

    def clearSol(self):
        self.sol = None
        self.update()

    def clearClicked(self):
        self.clicked = set()
        self.update()

    def updateSol(self, sol):
        self.sol = sol
        self.update()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawSol(qp)
        self.drawClicked(qp)
        qp.end()

    def drawClicked(self, qp):
        qp.setPen(QtGui.QPen(QtGui.QColor(255, 0, 0), 2))
        for (x1, y1) in self.clicked:
            qp.drawEllipse(x1-2, y1-2, 3, 3)

    def drawSol(self, qp):
        if self.sol is None:
            return

        qp.setPen(QtGui.QPen(QtGui.QColor(0, 255, 255), 1))

        g = self.sol

        for i in range(0, len(g)-1):
            #print((g[i  ][0], g[i+1][0], g[i  ][1], g[i+1][1]))
            qp.drawLine(g[i  ][0], g[i  ][1],
                        g[i+1][0], g[i+1][1])

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            x, y  = event.pos().x(), event.pos().y()
            print((x, y))
            self.clicked.add((x, y))
            self.update()
