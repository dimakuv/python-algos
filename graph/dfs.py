# Depth-First Search (DFS)

from collections import OrderedDict
from vertex import Vertex

class Graph(object):

    def __init__(self, G):
        self.G = G
        self.timestamp = 0
        self.finished = []
        self.SCCstring = ""

    def __str__(self):
        s = ""
        for v in self.G.keys():
            s += "%s: %d %s %d %d\n" % (v.name, v.level, str(v.parent), v.start, v.finish)
        return s

    def reset(self):
        self.finished = []
        self.timestamp = 0
        for v in self.G.keys():
            v.reset()

    def DFSvisit(self, s):
        self.timestamp += 1
        s.start = self.timestamp
        self.SCCstring += str(s) + ", "

        for v in self.G[s]:
            if v.start == None:
                v.level  = s.level + 1
                v.parent = s
                self.DFSvisit(v)

        self.timestamp += 1
        self.finished.append(s)
        s.finish = self.timestamp


    def DFS(self):
        self.reset()
        for v in self.G.keys():
            if v.start == None:
                self.SCCstring += "New SCC: "
                v.level = 0
                self.DFSvisit(v)
                self.SCCstring += "\n"

    def classifyedges(self):
        if self.timestamp == 0:
            print "Error: need to run DFS first!"
            return
        print "classifyedges:"
        for v in self.G.keys():
            for u in self.G[v]:
                print "  edge", str(v), str(u), ": ",
                if u.parent == v:
                    print "tree"
                elif v.start < u.start and v.finish > u.finish:
                    print "forward"
                elif v.start > u.start and v.finish < u.finish:
                    print "backward"
                else:
                    print "cross"

    def toposort(self):
        if self.timestamp == 0:
            print "Error: need to run DFS first!"
            return
        print "toposort:", "->".join([str(v) for v in reversed(self.finished)])

    def SCC(self):
        # step 1: run DFS and memorized finished times; O(V+E)
        self.DFS()
        # step 2: transpose original graph; O(V+E)
        # note how vertices are put in Gt in the G-finished order
        Gt = Graph(OrderedDict([(v, []) for v in reversed(self.finished)]))
        for v in self.G.keys():
            for u in self.G[v]:
                Gt.G.setdefault(u, []).append(v)
        print Gt
        # step 3: run DFS again on Gt
        Gt.DFS()
        print Gt.SCCstring


def test():
    a = Vertex('a'); s = Vertex('s'); c = Vertex('c'); d = Vertex('d'); b = Vertex('b'); g = Vertex('g');
    z = Vertex('z'); x = Vertex('x'); v = Vertex('v'); f = Vertex('f'); e = Vertex('e'); h = Vertex('h');
    # undirected graph
    G = Graph( OrderedDict([ (s,[a, x]), (a,[s, z]), (z,[a]), (x,[s, d, c]), (d,[x, c, f]), (c,[x,d,f,v]), (f,[d,c,v]), (v,[f,c]) ]) )
    G.DFS()
    G.classifyedges()
    G.toposort()  # bogus since graph is undirected and cyclic
    # directed graph
    G = Graph( OrderedDict([ (a,[b, c]), (b,[d]), (c,[d, f]), (d,[e]), (e,[]), (f,[]) ]) )
    G.DFS()
    G.classifyedges()
    G.toposort()
    G.SCC()
    # directed graph for SCC (from Cormen)
    G = Graph( OrderedDict([ (a,[b]), (b,[e,f,c]), (c,[g, d]), (d,[c, h]), (e,[a, f]), (f,[g]), (g,[f, h]), (h,[h]) ]) )
    G.SCC()
    # Prof. Bumstead gets dressed in the morning
    undershorts = Vertex('undershorts'); pants = Vertex('pants'); belt = Vertex('belt');
    shirt = Vertex('shirt'); tie = Vertex('tie'); jacket = Vertex('jacket'); watch = Vertex('watch');
    socks = Vertex('socks'); shoes = Vertex('shoes');
    Bumstead = Graph( OrderedDict([
            (undershorts, [pants, shoes]),
            (pants, [belt, shoes]),
            (belt, [jacket]),
            (shirt, [belt, tie]),
            (tie, [jacket]),
            (jacket, []),
            (socks, [shoes]),
            (shoes, []),
            (watch, [watch]),
        ]) )
    Bumstead.DFS()
    Bumstead.toposort()
