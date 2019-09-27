# -*- coding: utf-8 -*-
#Problem 009 - Special Pythagorean triplet
import itertools as it

#Solução com método por Itertools
numbers = [list(range(1, 500)), list(range(1, 500)), list(range(1, 500))]
combinations = list(it.combinations_with_replacement(numbers[0], 3))

def search2():
	for i in combinations:
		if i[0] + i[1] + i[2] == 1000 and i[0]**2 + i[1]**2 == i[2]**2:
			return i

#Solução com metodo linear
check = False
value = 0
def search():
	for i in range(1, 500):
		for j in range(1, 500):
			for k in range(1, 500):
				if i + j + k == 1000 and i**2 + j**2 == k**2:
					return [i, j, k]             

#No método itertools é gerada a lista completa de combinações
#Comparando as duas, o tempo para gerar a lista toda não compensa
#o método de brute force da geração linear

value = search()
final = value[0] * value[1] * value[2]
print(final)