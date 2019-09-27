# -*- coding: utf-8 -*-
#Problem 005 - Smallest multiple
a = 1
x = 100
digits = 20
value = 0

while True:
    if a <= digits:
        if not(x % a):
            if a == digits:
                value = x
                break
            else:
                a += 1
        else:
            a = 1
            x += 1

print(x)