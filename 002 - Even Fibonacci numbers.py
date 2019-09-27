# -*- coding: utf-8 -*-
#Problem 002 - Even Fibonacci numbers
a = 1
b = 1
c = 0
soma = 0

while c < 4000000:
	c = a + b
	a = b
	b = c

	if not(c % 2):
		soma += c

print(soma)