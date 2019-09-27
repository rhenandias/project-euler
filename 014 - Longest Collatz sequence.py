# -*- coding: utf-8 -*-
#Problem 014 - Longest Collatz sequence
def even(n):
    if not(n % 2):
        return True
    return False
    
def collatz(n):
    sequence = []
    while n > 1:
        if even(n):
            n /= 2
        else:
            n = (3 * n) + 1
        sequence.append(n)
    return sequence
    
last_amount = 0
last_number = 0
        
for i in range(1000000):
    seq = collatz(i)
    size = len(seq)
    if size > last_amount:
        last_amount = size
        last_number = i

print(last_number)
    