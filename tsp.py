import random
from math import exp, cosh, sqrt, log, e

class simmulatedAnnealing():
    def __init__(self):
        self.t_0         = 20.0
        self.t_n         = 0.0
        self.T           = 0.1
        self.maxIter     = 10**3
        self.stepPlot    = 10
        self.plotCounter = 0
        self.drawerTemp  = None
        self.drawerFunc  = None
        self.neighborFun = swap_adjacent
        self.tempFun     = linearTemp

    def setTempFunction(self, index):
        index += 1
        if index == 1:
            self.tempFun = linearTemp
        elif index == 2:
            self.tempFun = logTemp
        elif index == 3:
            self.tempFun = coshTemp

    def setSwapFunction(self, index):
        index += 1
        if index == 1:
            self.neighborFun = swap_adjacent
        elif index == 2:
            self.neighborFun = swap_2
        elif index == 3:
            self.neighborFun = move_1
        elif index == 4:
            self.neighborFun = shuffle_2p

    def setDrawer(self, temp, func):
        self.drawerFunc = func
        self.drawerTemp = temp
        self.drawerFunc.setLimits(self.t_0, self.t_n, self.maxIter)
        self.drawerTemp.setLimits(self.t_0, self.t_n, self.maxIter)

    def updateConfig(self, t0, tn, maxIter, plot):
        self.t_0      = t0
        self.t_n      = tn
        self.maxIter  = maxIter
        self.stepPlot = plot
        self.drawerFunc.setLimits(0   , 2200 , maxIter)
        self.drawerTemp.setLimits(t0  , tn, maxIter)

    def step(self, graph, steps = 10, s0 = None, i = None, improves = False):
        j       = 0
        i       = 0 if i is None else i
        s0      = randomSolution(graph) if s0 is None else s0

        t_0         = self.t_0
        t_n         = self.t_n
        T           = self.T
        maxIter     = self.maxIter
        plotCounter = self.plotCounter

        while i < maxIter and j < steps:
            T = self.tempFun(t_0, t_n, i, maxIter)
            sn = self.pertubate(s0.copy())
            esn = energy(sn)
            es0 = energy(s0)
            if exp(-(esn - es0)/T) > random.random():
                s0  = sn
                es0 = esn

            i += 1
            self.plotCounter += 1
            if self.plotCounter >= self.stepPlot or i == 1:
                self.plotCounter = 0
                self.drawerFunc.newPoint(i, es0)
                self.drawerTemp.newPoint(i, T)
            if not improves:
                j += 1

            if esn < es0 and improves:
                break

        return s0, energy(s0), i, T

    def pertubate(self, g):
        self.neighborFun(g)
        return g

def swap_adjacent(g):
    a    = random.randint(1, len(g) - 2)
    b    = a + 1
    p    = g[a]
    g[a] = g[b]
    g[b] = p
    return g

def swap_2(g):
    a    = random.randint(1, len(g) - 2)
    b    = random.randint(1, len(g) - 2)
    p    = g[a]
    g[a] = g[b]
    g[b] = p
    return g

def move_1(g):
    a     = random.randint(1, len(g) - 2)
    b     = random.randint(1, len(g) - 2)
    g.insert(b, g.pop(a))
    return g

def shuffle_2p(g):
    a, b = -1, -1
    while a >= b:
        a     = random.randint(1, len(g) - 4)
        b     = random.randint(1, len(g) - 3)
    g1 = g[:a ]
    g2 = g[a:b]
    g3 = g[b: ]
    random.shuffle(g2)
    gg = g1 + g2 + g3
    return gg

def energy(g):
    c = 0
    for i in range(0, len(g)-1):
        c += dist(g[i], g[i+1])

    return c

def dist(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def randomSolution(g):
    g2 = g.copy()
    random.shuffle(g2)
    g2.append(g2[0])
    return g2

def linearTemp(t_0, t_n, i, n):
    return t_0 - i * (t_0 - t_n) / n

def logTemp(t_0, t_n, i, n):
    return t_0 - i ** ( log(t_0 - t_n, e) / log(n, e) )

def coshTemp(t_0, t_n, i, n):
    return (t_0 - t_n) / cosh( 10.0 * i / n )

