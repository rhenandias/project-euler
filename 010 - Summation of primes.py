#Problema 010
from timeit import default_timer as timer
import math
    
def prime(n):
    if not(n % 2) and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not(n % i):
            return False
    return True
    
start = timer()

primes = [2]
for i in range(3, 2000000, 2):
    if prime(i):
        primes.append(i)
value = sum(primes)

end = timer()
exec_time = end - start

print value
print str(end - start) + " sec"

f = open('010 - Summation of primes.txt', 'w')
f.write(str(value) + '\n')
f.write(str(exec_time) + " sec" + '\n')
f.close()