#Problema 019

from math import floor

def compute_day(q, m, y):
    #Ajusta ano, caso meses seja janeiro ou fevereiro
    if m == 1 or m == 2: y -= 1
    #Zero-based month to Zeller's format
    month = [13, 14, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    return (q + floor((13*(month[m-1]+1))/5) + y + floor(y/4) - floor(y/100) + floor(y/400) ) % 7

sundays = 0
for ano in range(1901, 2001):
    for mes in range(1, 13):
        dia = compute_day(1, mes, ano)
        if dia == 0:
            sundays += 1
            
print(sundays)