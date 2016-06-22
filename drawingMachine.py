from PyQt4              import *

class drawingMachine(QtGui.QWidget):
    def __init__(self, parent = None):
        super(drawingMachine, self).__init__(parent)
        self.clicked  = set()
        self.sol      = None
        self.x        = []
        self.fx       = []
        self.t0       = 900000
        self.tn       = 10
        self.maxIter  = 1000
        self.isTemp   = True

    def setIsTemp(self, x):
        self.isTemp = x

    def clearData(self):
        self.x  = []
        self.fx = []
        self.update()

    def setLimits(self, t0, tn, maxIter):
        self.t0      = t0
        self.tn      = tn
        self.maxIter = maxIter

    def newPoint(self, x, fx):
        self.x.append(x)
        self.fx.append(fx)
        self.update()

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
        self.drawData(qp)
        self.drawSol(qp)
        self.drawClicked(qp)
        qp.end()

    def drawClicked(self, qp):
        qp.setPen(QtGui.QPen(QtGui.QColor(255, 0, 0), 1))
        for (x1, y1) in self.clicked:
            qp.drawEllipse(x1-2, y1-2, 3, 3)

    def drawSol(self, qp):
        if self.sol is None:
            return

        qp.setPen(QtGui.QPen(QtGui.QColor(0, 255, 255), 1))
        g = self.sol
        for i in range(0, len(g)-1):
            qp.drawLine(g[i  ][0], g[i  ][1],
                        g[i+1][0], g[i+1][1])

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            x, y  = event.pos().x(), event.pos().y()
            self.clicked.add((x, y))
            self.update()

    def drawData(self, qp):
        qp.setPen(QtGui.QPen(QtGui.QColor(255, 0, 0), 1))
        size = self.size()

        if not self.isTemp and len(self.x) > 0:
            self.tn = self.fx[0]
            self.t0 = self.fx[0]
            for i in self.fx:
                self.tn = min(self.tn, i + 10)
                self.t0 = max(self.t0, i + 0 )

        for k, v in enumerate(zip(self.x, self.fx)):
            if k >= len(self.x) - 1:
                continue
            x1, y1 = self.x[k+0], self.fx[k+0]
            x2, y2 = self.x[k+1], self.fx[k+1]
            if self.isTemp:
                y1 = int(size.height() - ( y1 - self.tn ) / ( self.t0 - self.tn + 1 ) * size.height())
                y2 = int(size.height() - ( y2 - self.tn ) / ( self.t0 - self.tn + 1 ) * size.height())
            else:
                y1 = int(size.height() - ( y1 - self.tn ) / ( self.t0 - self.tn + 1 ) * size.height())
                y2 = int(size.height() - ( y2 - self.tn ) / ( self.t0 - self.tn + 1 ) * size.height())

            x1 = int(( x1           ) / ( self.maxIter      ) * size.width() )
            x2 = int(( x2           ) / ( self.maxIter      ) * size.width() )
            qp.drawLine(x1, y1, x2, y2)

