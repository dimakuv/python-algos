# shortest path for graphs with negative cycles

from collections import OrderedDict
from spvertex import SPVertex

def shortestpath(G, W, s):
    """shortest path from start vertex s to all reachable vertices or False if found neg cycle"""
    # initialize
    for v in G.keys():
        v.reset()
    s.dist = 0
    # go through all vertices |V|-1 times and relax their edges;  O(VE) ~= O(V^3)
    for _ in range(len(G.keys())-1):
        for u in G.keys():
            for i, v in enumerate(G[u]):
                v.relax(u, W[u][i])
    # one last iteration to check for negative cycles
    # (if some v.dist didn't converge after |V|-1, it's due to neg cycle)
    for u in G.keys():
        for i, v in enumerate(G[u]):
            if (v.dist is not None and u.dist is not None
                and v.dist > u.dist + W[u][i]):
                return False
    return True

def printshortestpath(s, t):
    """print shortest path from s to t; shortestpath(.., s) must be run previously"""
    if t.dist is None:
        print "No path found from %s to %s" % (str(s), str(t))
        return
    sp = [t]
    while sp[-1].pi:
        sp.append(sp[-1].pi)
    print "shortestpath:", "->".join([str(v) for v in reversed(sp)]), "(dist = %d)" % t.dist

def findprintshortestpath(G, W, s, t):
    if shortestpath(G, W, s):
        printshortestpath(s, t)
    else:
        print "Found negative cycle, cannot compute"


def test():
    a = SPVertex('a'); b = SPVertex('b'); c = SPVertex('c'); d = SPVertex('d'); e = SPVertex('e'); f = SPVertex('f');
    g = SPVertex('g'); h = SPVertex('h'); i = SPVertex('i'); j = SPVertex('j'); k = SPVertex('k'); l = SPVertex('l');
    G = OrderedDict([ (a,[b, c]), (b,[c, d]), (c,[d, e, f]), (d,[ e, f]), (e,[ f]), (f,[]) ])
    W = OrderedDict([ (a,[5, 3]), (b,[2, 6]), (c,[7, 4, 2]), (d,[-1, 1]), (e,[-2]), (f,[]) ])
    findprintshortestpath(G, W, b, f)
    # simple neg cycle example
    G = OrderedDict([ (a,[ b]), (b,[ c]), (c,[ d]), (d,[ b]) ])
    W = OrderedDict([ (a,[-2]), (b,[-2]), (c,[-2]), (d,[-2]) ])
    findprintshortestpath(G, W, a, d)
