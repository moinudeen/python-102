
import random
import string
import time


chars = string.ascii_lowercase
x = ''.join(random.choice(chars) for x in range(random.randint(8, 10)))



lower = []
for i in range(5000):
    x = ''.join(random.choice(chars) for x in range(random.randint(8, 10)))
    lower.append(x)


st= time.time()
caps = [] 
for word in lower:
    caps.append(word.upper())
print 'time taken: ',time.time()-st

st= time.time()
caps1 = map(str.upper,lower)
print 'time taken: ',time.time()-st





