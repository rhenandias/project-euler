# -*- coding: utf-8 -*-
#Problem 013 - Large sum
data = []
with open ('013 - Large sum - Data.txt', 'r') as data_file:
    for line in data_file:
        data.append(int(line))
        
data = str(sum(data))
print(data[:10])