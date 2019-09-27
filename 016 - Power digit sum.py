#Problema 016
from timeit import default_timer as timer

start = timer()

n = 2**1000
n = map(int, str(n))
soma = sum(n)

end = timer()
exec_time = end - start

print soma
print str(exec_time) + " sec"

f = open('016 - Power digit sum.txt', 'w')
f.write(str(soma) + '\n')
f.write(str(exec_time) + " sec" + '\n')
f.close()




    