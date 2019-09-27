#Problema 007
from timeit import default_timer as timer
import math

def primo(n):
    if not(n % 2) and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not(n % i):
            return False
    return True
    
start = timer()

primes = [2]

a = 3
b = 0
while b < 10001:
    if primo(a):
        primes.append(a)
        b += 1
    a += 2

end = timer()
exec_time = end - start

print primes[10000]
print str(exec_time) + " sec"

f = open('007 - 10001st prime.txt', 'w')
f.write(str(primes[10000]) + '\n')
f.write(str(exec_time) + " sec" + '\n')
f.close()