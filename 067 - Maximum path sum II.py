# -*- coding: utf-8 -*-
#problem 067 - Maximum path sum II
import numpy as np

triangle = [[int(i) for i in line.split()] for line in open('067 - Maximum path sum II - Data.txt')]

size = len(triangle)

for linha in range(1, size + 1):
    for i in range(len(triangle[-linha]) - 1):
        soma1 = triangle[-linha][i]   + triangle[-(linha+1)][i]
        soma2 = triangle[-linha][i+1] + triangle[-(linha+1)][i]
        soma = max(soma1, soma2)
        triangle[-(linha+1)][i] = soma
        
print(triangle[0][0])