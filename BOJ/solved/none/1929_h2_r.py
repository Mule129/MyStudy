#에라토스테네스의 체
n, m = map(int, input().split())

data = [True]* (m+1)

for i in range(2, m+1):
    
    if data[i] == True:
        for x in range(i+i, m+1, i):
            #print(i, x)
            data[x] = False

for i, x in enumerate(data):
    
    if x == True and i >= max(2, n):
        print(i)