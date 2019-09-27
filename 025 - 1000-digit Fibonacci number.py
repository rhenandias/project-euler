# -*- coding: utf-8 -*-
#Problem 025 - 1000-digit Fibonacci number
a = 1
b = 1
c = 0
index = 2

while True:
    c = a + b
    a = b
    b = c
    index += 1
    
    if len(str(c)) >= 1000:
        break

print(index)