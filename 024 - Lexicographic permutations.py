#Problema 024

import itertools

permut = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

permut = "".join(map(str, permut[1000000 - 1]))

print(permut)