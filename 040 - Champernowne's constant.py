# -*- coding: utf-8 -*-
#Problema 040 - Champernowne's constant
l = ""
i = 0
 
while len(l) < 1000000:
    i += 1
    l += str(i)

acc = 1
for i in(0, 9, 99, 999, 9999, 99999, 999999):
    acc *= int(l[i])
     
print(acc)