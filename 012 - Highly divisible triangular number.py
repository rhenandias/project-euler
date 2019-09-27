# -*- coding: utf-8 -*-
#Problem 012 - Highly divisible triangular number
import math

def gen_primes(n):
    primes = [2]
    i = 3
    while len(primes) < n:
        if primo(i):
            primes.append(i)
        i += 2
    return primes
    
def primo(n):
    if not(n % 2) and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not(n % i):
            return False
    return True

def fatorar(n, primos):
    factors = []
    i = 0
    while n > 1:
        if not(n % primos[i]):
            factors.append(primos[i])
            n = n / primos[i]
        else:
            i += 1 
    return factors
    
def triangle(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma
    
primes = gen_primes(10000)    
    
divisors = 1
a = 1
while divisors < 500:
    a += 1
    
    triang = triangle(a)
    
    fatores = fatorar(triang, primes)
    last_prime_index = primes.index(fatores[-1])

    divisors = 1
    for i in range(last_prime_index + 1):
        divisors *= (fatores.count(primes[i]) + 1)

number = triang
print(number)