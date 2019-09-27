#Problema 005
from timeit import default_timer as timer
start = timer()

a = 1
x = 100
digits = 20
value = 0

while True:
    if a <= digits:
        if not(x % a):
            if a == digits:
                value = x
                break
            else:
                a += 1
        else:
            a = 1
            x += 1

end = timer()
exec_time = end - start

print x
print str(exec_time) + " sec"

f = open('005 - Smallest multiple.txt', 'w')
f.write(str(value) + '\n')
f.write(str(exec_time) + " sec" + '\n')
f.close()