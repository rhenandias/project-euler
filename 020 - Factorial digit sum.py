# -*- coding: utf-8 -*-
#Problem 020 - Factorial digit sum
from math import factorial

a = factorial(100)
a = map(int, str(a))
soma = sum(a)
print(soma)

    