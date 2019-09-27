#Problema 004
from timeit import default_timer as timer
start = timer()

start = timer()

products = []
for i in range(1, 1000):
    for j in range(1, 1000):
        products.append(str(i * j))
    
palindromes = []
for k in products:
    if k == k[::-1]:
        palindromes.append(int(k))
        
end = timer()
exec_time = end - start

print max(palindromes)
print str(exec_time) + " sec"

f = open('004 - Largest palindrome product.txt', 'w')
f.write(str(max(palindromes)) + '\n')
f.write(str(exec_time) + " sec" + '\n')
f.close()
        
