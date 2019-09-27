# -*- coding: utf-8 -*-
#Problem 048 - Self powers
l = []

for i in range(1, 1000):
    l.append(i**i)
    
l = str(sum(l))

print(l[-10:])
