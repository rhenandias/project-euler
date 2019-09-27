#Problema 006
from timeit import default_timer as timer
start = timer()

s1 = 0
for i in range(101):
    s1 += i**2
    
s2 = 0
for i in range(101):
    s2 += i

end = timer()
exec_time = end - start

print (s2**2) - s1
print str(exec_time) + " sec"

f = open('006 - Sum square difference.txt', 'w')
f.write(str((s2**2) - s1) + '\n')
f.write(str(exec_time) + " sec" + '\n')
f.close()