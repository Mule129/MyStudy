import time
print("start")
t1 = time.time()
for i in range(int((2**31)/20)):
    pass
t2 = time.time()
print(t2-t1)