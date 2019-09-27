# -*- coding: utf-8 -*-
#Problem 006 - Sum square difference
s1 = 0
for i in range(101):
    s1 += i**2
    
s2 = 0
for i in range(101):
    s2 += i

print((s2**2) - s1)