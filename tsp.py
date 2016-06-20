import random
from math import exp, cosh, sqrt

class simmulatedAnnealing():
    def __init__(self):
        self.t_0     = 20.0
        self.t_n     = 0.0
        self.T       = 0.1
        self.maxIter = 10**3

    def updateConfig(self, t0, tn, maxIter):
        self.t_0     = t0
        self.t_n     = tn
        self.maxIter = maxIter

    def step(self, graph, steps = 10, s0 = None, i = None, improves = False):
        j       = 0
        i       = 0 if i is None else i
        s0      = randomSolution(graph) if s0 is None else s0

        t_0     = self.t_0
        t_n     = self.t_n
        T       = self.T
        maxIter = self.maxIter

        while i < maxIter and j < steps:
            T =  (t_0 - t_n)/cosh((10.0*float(i)/float(maxIter)))
            sn = pertubate(s0.copy())
            esn = energy(sn)
            es0 = energy(s0)
            if exp(-(esn - es0)/T) > random.random():
                s0 = sn

            i += 1
            if not improves:
                j += 1

            print(i, energy(s0), T)

            if esn < es0 and improves:
                break

        return s0, energy(s0), i, T

def pertubate(g):
    a    = random.randint(1, len(g) - 2)
    b    = random.randint(1, len(g) - 2)
    p    = g[a]
    g[a] = g[b]
    g[b] = p
    return g

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
