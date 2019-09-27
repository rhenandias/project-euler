#Problema 025
from timeit import default_timer as timer
start = timer()

a = 1
b = 1
c = 0
index = 2

while True:
    c = a + b
    a = b
    b = c
    index += 1
    
    if len(str(c)) >= 1000:
        break

end = timer()
exec_time = end - start

print index
print str(exec_time) + " sec"

f = open('025 - 1000-digit Fibonacci number.txt', 'w')
f.write(str(index) + '\n')
f.write(str(exec_time) + " sec" + '\n')
f.close()