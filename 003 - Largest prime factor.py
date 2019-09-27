# -*- coding: utf-8 -*-
#Problem 003 - Largest prime factor
import math

def primo(n):
    if not(n % 2) and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not(n % i):
            return False
    return True

prime_factor = 0
x = 600851475143
a = 1

while x > 1:
    if primo(a) and not(x % a):
        prime_factor = a
        x = x/a
    a += 1
    

print(prime_factor)