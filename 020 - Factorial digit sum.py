#Problema 020
from timeit import default_timer as timer
from math import factorial

start = timer()

a = factorial(100)
a = map(int, str(a))
soma = sum(a)

end = timer()
exec_time = end - start

print soma
print str(exec_time) + " sec"

f = open('020 - Factorial digit sum.txt', 'w')
f.write(str(soma) + '\n')
f.write(str(exec_time) + " sec" + '\n')
f.close()




    