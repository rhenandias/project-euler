# -*- coding: utf-8 -*-
#Problem 034 - Digit factorials
from math import factorial

soma = 0
for i in range(3, 100000):
	digits = [factorial(int(j)) for j in str(i)]
	if sum(digits) == i:
		soma += i

print(soma)