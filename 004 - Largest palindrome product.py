# -*- coding: utf-8 -*-
#Problem 004 - Largest palindrome product
products = []
for i in range(1, 1000):
    for j in range(1, 1000):
        products.append(str(i * j))
    
palindromes = []
for k in products:
    if k == k[::-1]:
        palindromes.append(int(k))

print(max(palindromes))