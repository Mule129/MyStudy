import time
import math

data = int(input())
time_1 = time.time()
data -= 1



value = 0
t = math.ceil(data/6)
dump = 0

for i in range(t+1):
    dump += i
    if dump >= t:
        value = i
        break

print(value+1)
time_2 = time.time()
print(time_2, time_1)