T = int(input())

line = [i for i in range(15)]
for _ in range(T):
    k = int(input())
    n = int(input())
    for i in range(k):
        for x in range(1, n+1):
            line[x] = line[x-1] + line[x]
            if x == n and i == k-1:
                print(line[x])
    line = [i for i in range(15)]
    if k == 0:
        print(n)