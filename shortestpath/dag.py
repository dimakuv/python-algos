# shortest path for a special case of DAGs
#   -> enough to do toposort and relax each edge

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from collections import OrderedDict
from spvertex import SPVertex
from graph.dfs import Graph

def shortestpath(G, W, s, t):
    """shortest path from start vertex s to end vertex t"""
    GDFS = Graph(G)
    GDFS.DFS()  # O(V+E)

    started = False
    for u in reversed(GDFS.finished):  # O(V+E)
        if u == s:
            u.dist = 0
            started = True
        if not started:
            continue
        if u == t:
            break
        for i, v in enumerate(G[u]):
            v.relax(u, W[u][i])
    else:
        if started:  print "No path found from %s to %s" % (str(s), str(t))
        else:        print "No start vertex %s found" % str(s)
        return

    sp = [t]
    while sp[-1].pi:
        sp.append(sp[-1].pi)
    print "shortestpath:", "->".join([str(v) for v in reversed(sp)]), "(dist = %d)" % t.dist


def test():
    a = SPVertex('a'); b = SPVertex('b'); c = SPVertex('c'); d = SPVertex('d'); e = SPVertex('e'); f = SPVertex('f');
    g = SPVertex('g'); h = SPVertex('h'); i = SPVertex('i'); j = SPVertex('j'); k = SPVertex('k'); l = SPVertex('l');
    G = OrderedDict([ (a,[b, c]), (b,[c, d]), (c,[d, e, f]), (d,[ e, f]), (e,[ f]), (f,[]) ])
    W = OrderedDict([ (a,[5, 3]), (b,[2, 6]), (c,[7, 4, 2]), (d,[-1, 1]), (e,[-2]), (f,[]) ])
    shortestpath(G, W, b, f)
