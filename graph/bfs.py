# Breadth-First Search (BFS)

from collections import deque
from vertex import Vertex

class Graph(object):

    def __init__(self, G):
        self.G = G

    def __str__(self):
        s = ""
        for v in self.G.keys():
            s += "%s: %d %s %d %d\n" % (v.name, v.level, str(v.parent), v.start, v.finish)
        return s

    def reset(self):
        for v in self.G.keys():
            v.reset()

    def BFS(self, s):
        self.reset()
        queue = deque([s])
        s.level = 0
        s.start = 0

        timestamp = 0
        while len(queue):
            v = queue.popleft()
            for u in self.G[v]:
                if u.start == None:
                    u.level  = v.level + 1
                    u.parent = v
                    timestamp += 1
                    u.start  = timestamp
                    queue.append(u)
            timestamp += 1
            v.finish = timestamp

    def shortestpath(self, s, f):
        path = []
        v = f
        while v:
            path.append(v)
            if v == s:  break
            v = v.parent
        else:
            print "shortest path:", "No path from", str(s), "to", str(f)
            return
        print "shortest path:", "->".join([str(v) for v in reversed(path)])


def test():
    a = Vertex('a'); s = Vertex('s'); c = Vertex('c'); d = Vertex('d'); b = Vertex('b');
    z = Vertex('z'); x = Vertex('x'); v = Vertex('v'); f = Vertex('f'); e = Vertex('e');
    # undirected graph
    G = Graph( { a: [s, z], z: [a], s: [a, x], x: [s, d, c], d: [x, c, f], c: [x,d,f,v], f: [d,c,v], v: [f,c] } )
    G.BFS(s)
    G.shortestpath(s, f)
    G.shortestpath(s, v)
    G.shortestpath(s, z)
    # directed graph
    G = Graph( { a: [b, c], b: [d], c: [d, f], d: [e], e: [], f: [] } )
    G.BFS(a)
    G.shortestpath(a, e)
    G.shortestpath(a, f)
    G.shortestpath(s, e)
