# -*- coding: utf-8 -*-
#Problema 035 - Circular primes
import math

def primo(n):
    if not(n % 2) and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not(n % i):
            return False
    return True
    
def rotate(ls, n):
    return ls[n:] + ls[:n]

circular = [2]

for i in range(3, 1000000, 2):
    if primo(i):
        check = 0
        maped = list(map(int, str(i)))
        size = len(maped)
    
        for j in range(size):
            rotation = rotate(maped, j)
            rotation = ''.join(list(map(str, rotation)))
            if primo(int(rotation)):
                check += 1
        if check == size:
            circular.append(i)
            
print(len(circular))