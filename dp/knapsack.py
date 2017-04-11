# knapsack

HUGENUM = 2**30  # substitute for +Inf, for simplicity

class Item(object):
    def __init__(self, name, value, weight):
        self.name   = name
        self.value  = value
        self.weight = weight

def knapsack(items, S):
    dp  = {}  # dict of (item idx, remaining S) -> (maximized value, item taken)
    val = knapsack_recurse(dp, items, 0, S)
    print "for capacity: ", S, "maximum value:", val, "   items:",
    for idx, item in enumerate(items):
        if S <= 0:  break
        if dp[(idx, S)][1] == True:
            S -= items[idx].weight
            print items[idx].name,
    print

def knapsack_recurse(dp, items, i, S):
    if S < 0:
        return -HUGENUM
    if i == len(items):
        return 0
    if dp.get((i, S)) is not None:
        return dp[(i, S)][0]
    taken    = items[i].value + knapsack_recurse(dp, items, i+1, S - items[i].weight)
    nottaken = knapsack_recurse(dp, items, i+1, S)
    if taken > nottaken:
        dp[(i, S)] = (taken, True)
        return taken
    dp[(i, S)] = (nottaken, False)
    return nottaken

def test():
    items = [
        Item("green",  4,  12), 
        Item("gray",   2,  1), 
        Item("yellow", 10, 4), 
        Item("blue",   2,  2), 
        Item("red",    1,  1), 
    ]
    knapsack(items, 15)
    knapsack(items, 5)

    items = [
        Item("ring",       15, 1), 
        Item("candelabra", 10, 5), 
        Item("radio",      9,  3), 
        Item("elvis",      5,  4), 
    ]
    knapsack(items, 8)
