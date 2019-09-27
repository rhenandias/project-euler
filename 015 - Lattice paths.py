# -*- coding: utf-8 -*-
#Problem 015 - Lattice paths
import math
n = 20
paths = math.factorial(2 * n)/(math.factorial(n)**2)
print(paths)