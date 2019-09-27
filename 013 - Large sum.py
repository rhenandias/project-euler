#Problema 013
from timeit import default_timer as timer

start = timer()

data = []

with open ('013 - Large sum - Data.txt', 'r') as data_file:
    for line in data_file:
        data.append(int(line))
        
data = str(sum(data))

end = timer()
exec_time = end - start

print data[:10]
print str(exec_time) + " sec"

f = open('013 - Large sum.txt', 'w')
f.write(str(data[:10]) + '\n')
f.write(str(exec_time) + " sec" + '\n')
f.close()
