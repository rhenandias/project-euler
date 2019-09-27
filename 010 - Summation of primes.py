# -*- coding: utf-8 -*-
#Problemm 010 - Summation on primes
import math
    
def prime(n):
    if not(n % 2) and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not(n % i):
            return False
    return True

value = 2
for i in range(3, 2000000, 2):
    if prime(i):
        value += i

print(value)