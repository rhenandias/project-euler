#Problema 017

with open("data.txt", 'r') as f:
    data = f.readlines()

alphabet = "abcdefghijklmnopqrstuvwxyz"
         
c = 0

for i in data:
    for j in i:
        if j in alphabet:
            c += 1

print(c)
    