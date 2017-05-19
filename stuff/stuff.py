# random simple math problems

# Greatest Common Divisor (GCD), Euclidean method (division)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Least Common Multiple (LCM), via GCD
def lcm(a, b):
    if a == 0 and b == 0:
        return 0
    return abs(a*b)/gcd(a, b)

# side of the line determined by (xa,ya) and (xb,yb) on which point (x,y) lies
# returns positive number if on "plus" side, negative if on "neg" side, 0 if on line
def pointside(xa, ya, xb, yb, x, y):
    return (xa-xb)*(y-ya) - (ya - yb)*(x-xa)

def test():
    pairs = [(0, 0), (0, 1), (1, 0), (21, 6), (1071, 462), (462, 1071), (1386, 3213)]
    for a,b in pairs:
        print "%d\t%d\t: gcd=%d\t lcm=%d" % (a, b, gcd(a,b), lcm(a,b))

    points = [(0, 0), (2, 2), (2, 1), (1, 2), (3, 1), (2, 3)]
    for x,y in points:
        print "line from (%d,%d) and (%d,%d): point (%d,%d) is on side %d" % \
                (1,1, 3,3, x,y, pointside(1, 1, 3, 3, x, y))
