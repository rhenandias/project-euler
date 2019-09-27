# -*- coding: utf-8 -*-
#Problem 007 - 10001st prime
import math

def primo(n):
    if not(n % 2) and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not(n % i):
            return False
    return True
    
primes = [2]

a = 3
b = 0
while b < 10001:
    if primo(a):
        primes.append(a)
        b += 1
    a += 2

print(primes[10000])
