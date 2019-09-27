#Problema 034

from math import factorial

soma = 0

for i in range(3, 100000):
	digits = [factorial(int(j)) for j in str(i)]
	if sum(digits) == i:
		soma += i

print soma