#Problema 001
from timeit import default_timer as timer
start = timer()

soma = 0
for i in range(1000):
	if not(i % 3) or not(i % 5):
		soma += i

end = timer()
exec_time = end - start

print soma
print str(exec_time) + " sec"

f = open('001 - Multiples of 3 and 5.txt', 'w')
f.write(str(soma) + '\n')
f.write(str(exec_time) + " sec" + '\n')
f.close()