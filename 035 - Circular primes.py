#Problema 035
from timeit import default_timer as timer
import math

def primo(n):
    if not(n % 2) and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not(n % i):
            return False
    return True
    
def rotate(ls, n):
    return ls[n:] + ls[:n]
    
start = timer()

circular = [2]

for i in xrange(3, 1000000, 2):
    if primo(i):
        check = 0
        maped = map(int, str(i))
        size = len(maped)
    
        for j in range(size):
            rotation = rotate(maped, j)
            rotation = ''.join(map(str, rotation))
            if primo(int(rotation)):
                check += 1
        if check == size:
            circular.append(i)
            
end = timer()
exec_time = end - start

print len(circular)
print str(exec_time) + " sec"

f = open('035 - Circular primes.txt', 'w')
f.write(str(len(circular)) + '\n')
f.write(str(exec_time) + " sec" + '\n')
f.close()