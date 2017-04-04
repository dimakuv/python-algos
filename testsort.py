#!/usr/bin/env python

import sys
import random
import importlib

def baseline(a):
    a.sort()
    return a

def test(a):
    print SORTFUNCSTR, ":  ",
    print a,

    a = SORTFUNC(a)

    # check invariant
    for i in range(1, len(a)):
        assert a[i] >= a[i-1]

    print "  -->  ",
    print a


SORTFUNC    = baseline
SORTFUNCSTR = "baseline"
if len(sys.argv) > 1:
    SORTFUNCSTR = sys.argv[1]
    SORTMODULE  = importlib.import_module(SORTFUNCSTR)
    SORTFUNC    = SORTMODULE.sort

test([0,1,2,3,4,5,6,7,8,9])
test([9,8,7,6,5,4,3,2,1,0])
test([1,1,1,1,1,1,1,1,1,1])
test([1,2,3,4,3,2,1,4,3,2])
test([int(10*random.random()) for i in xrange(10)])

try:
    test(SORTMODULE.testlist)
except:
    pass
