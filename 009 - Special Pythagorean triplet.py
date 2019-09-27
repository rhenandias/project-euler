#Problema 9
from timeit import default_timer as timer
start = timer()

check = False
value = 0

for i in range(1, 500):
    for j in range(1, 500):
        for k in range(1, 500):
            if i + j + k == 1000 and i**2 + j**2 == k**2:
                value = [i, j, k]
                check = True
            if check:
                break
        if check:
            break
    if check:
        break                

final = value[0] * value[1] * value[2]

end = timer()
exec_time = end - start

print final
print str(exec_time) + " sec"

f = open('009 - Special Pythagorean triplet.txt', 'w')
f.write(str(final) + '\n')
f.write(str(exec_time) + " sec" + '\n')
f.close()

                
