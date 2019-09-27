# -*- coding utf-8 -*-
#Problem 011 - Largest product in a grid

with open('011 - Largest product in a grid - Data.txt') as f:
    data = [i.split() for i in f.readlines()]

for i in range(20):
    data[i] = [int(j) for j in data[i]]
    
largest = 0
hold = 0

for i in range(20):
    for j in range(20):
        
        #Lateral 
        if j + 3 <= 19:
            hold = data[i][j] * data[i][j+1] * data[i][j+2] * data[i][j+3]
            largest = max(largest, hold)
        
        #Baixo 
        if i + 3 <= 19:
            hold = data[i][j] * data[i+1][j] * data[i+2][j] * data[i+3][j]
            largest = max(largest, hold)
        
        #Diagonal 1
        if i + 3 <= 19 and j + 3 <= 19:
            hold = data[i][j] * data[i+1][j+1] * data[i+2][j+2] * data[i+3][j+3]
            largest = max(largest, hold)
            
        #Diagonal 2
        if i - 3 >= 0 and j + 3 <= 19:
            hold = data[i][j] * data[i-1][j+1] * data[i-2][j+2] * data[i-3][j+3]
            largest = max(largest, hold)
            
        #Diagonal 3
        if i - 3 >= 0 and j - 3 >= 0:
            hold = data[i][j] * data[i-1][j-1] * data[i-2][j-2] * data[i-3][j-3]
            largest = max(largest, hold)
            
        #Diagonal 3
        if i + 3 <= 19 and j - 3 >= 0:
            hold = data[i][j] * data[i+1][j-1] * data[i+2][j-2] * data[i+3][j-3]
            largest = max(largest, hold)
            
print(largest)