# -*- coding: utf-8 -*-
#Problem 024 - Lexicograpgic permutations
import itertools as it

permut = list(it.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
permut = "".join(map(str, permut[1000000 - 1]))
print(permut)