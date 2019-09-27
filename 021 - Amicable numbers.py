# -*- coding: utf-8 -*-
#Problem 021 - Amicable numbers
def sum_divisors(n):
    divisors = 0
    for i in range(1, n):
        if not(n % i):
            divisors += i
    return divisors

amicables = []

for i in range(1, 10000):
    a = sum_divisors(i)
    b = sum_divisors(a)
    
    if b == i and i != a:
        amicables.append(i)
        amicables.append(a)
            
amicables = list(set(amicables))

print(sum(amicables))