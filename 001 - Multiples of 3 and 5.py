# -*- coding: utf-8 -*-
#Problem 001 - Multiples of 3 and 5
soma = 0
for i in range(1000):
	if not(i % 3) or not(i % 5):
		soma += i

print(soma)