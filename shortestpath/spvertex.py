# vertex class augmented for shortest path problem

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from graph.vertex import Vertex

class SPVertex(Vertex):

    def __init__(self, name):
        Vertex.__init__(self, name)
        self.dist = None  # current shortest path distance
        self.pi   = None  # parent for shortest path

    def reset(self):
        Vertex.reset(self)
        self.dist = None
        self.pi   = None

    def relax(self, u, w):
        """relax vertex reachable from u via edge with weight w"""
        if u.dist is None:
            return
        if self.dist is None or self.dist > u.dist + w:
            self.dist = u.dist + w
            self.pi   = u
