# shortest path for graphs without negative cycles
# NOTE: we use a simple list instead of minheap for simplicity;
#       this gives O(V^2 + E) = O(V^2)

from collections import OrderedDict
from spvertex import SPVertex

def extractmin(queue):
    # find vertex with minimal distance;  O(V)
    resi,resv = 0,queue[0]
    for i,v in enumerate(queue):
        if v.dist is not None and (resv.dist is None or v.dist < resv.dist):
            resi = i
            resv = v
    # remove this vertex from queue (don't care about order)
    queue[resi], queue[-1] = queue[-1], queue[resi]
    del queue[-1]
    return resv

def shortestpath(G, W, s, t=None):
    """shortest path from start vertex s to end vertex t (or to all reachable if t=None)"""
    # initialize
    for v in G.keys():
        v.reset()
    s.dist = 0
    # go through all vertices in order of increasing dist and relax their edges;  O(V^2)
    queue = G.keys()
    while len(queue) > 0:
        u = extractmin(queue)
        if t == u:
            break
        for i, v in enumerate(G[u]):
            v.relax(u, W[u][i])

def printshortestpath(s, t):
    """print shortest path from s to t; shortestpath(.., s) must be run previously"""
    if t.dist is None:
        print "No path found from %s to %s" % (str(s), str(t))
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
    shortestpath(G, W, b)
    printshortestpath(b, f)