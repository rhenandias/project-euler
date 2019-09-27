#Problema 002
from timeit import default_timer as timer
start = timer()

a = 1
b = 1
c = 0
soma = 0

while c < 4000000:
	c = a + b
	a = b
	b = c

	if not(c % 2):
		soma += c

end = timer()
exec_time = end - start

print soma
print str(exec_time) + " sec"

f = open('002 - Even Fibonacci numbers - Log.txt', 'w')
f.write(str(soma) + '\n')
f.write(str(exec_time) + " sec" + '\n')
f.close()