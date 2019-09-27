#Problema 008
from timeit import default_timer as timer

start = timer()

data = []

with open ('008 - Largest product in a series - Data.txt', 'r') as data_file:
    for line in data_file:
        for i in line:
            if i != '\n':
                data.append(int(i))

value = 0
for i in range(len(data) - 12):
    new_value = 1
    for j in range(13):
        new_value *= data[i + j]
    if new_value > value:
        value = new_value

end = timer()
exec_time = end - start

print value
print str(exec_time) + " sec"

f = open('008 - Largest product in a series.txt', 'w')
f.write(str(value) + '\n')
f.write(str(exec_time) + " sec" + '\n')
f.close()
        