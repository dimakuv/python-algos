#!/usr/bin/env python

import sys
import random
import importlib

try:
	MODULE = importlib.import_module(sys.argv[1])
	test = getattr(MODULE, "test")
	print "=====", sys.argv[1], "test ====="
except:
	print "[do nothing]"
	sys.exit(0)

MODULE.test()
