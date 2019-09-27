#Problema 003
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

prime_factor = 0
x = 600851475143
a = 1

while x > 1:
    if primo(a) and not(x % a):
        prime_factor = a
        x = x/a
    a += 1
    
end = timer()
exec_time = end - start

print prime_factor
print str(exec_time) + " sec"

f = open('003 - Largest prime factor.txt', 'w')
f.write(str(prime_factor) + '\n')
f.write(str(exec_time) + " sec" + '\n')
f.close()