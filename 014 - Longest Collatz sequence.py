#Problema 014
from timeit import default_timer as timer

def even(n):
    if not(n % 2):
        return True
    return False
    
def collatz(n):
    sequence = []
    while n > 1:
        if even(n):
            n /= 2
        else:
            n = (3 * n) + 1
        sequence.append(n)
    return sequence
    
start = timer()

last_amount = 0
last_number = 0
        
for i in xrange(1000000):
    seq = collatz(i)
    size = len(seq)
    if size > last_amount:
        last_amount = size
        last_number = i
        
end = timer()
exec_time = end - start

print last_number
print str(exec_time) + " sec"

f = open('014 - Longest Collatz sequence.txt', 'w')
f.write(str(last_number) + '\n')
f.write(str(exec_time) + " sec" + '\n')
f.close()

    