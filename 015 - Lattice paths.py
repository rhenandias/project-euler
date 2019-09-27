#Problema 015
from timeit import default_timer as timer
import math

start = timer()

n = 20
paths = math.factorial(2 * n)/(math.factorial(n)**2)

end = timer()
exec_time = end - start

print paths
print str(exec_time) + " sec"


f = open('015 - Lattice paths.txt', 'w')
f.write(str(paths) + '\n')
f.write(str(exec_time) + " sec" + '\n')
f.close()



    