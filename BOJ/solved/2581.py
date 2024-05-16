n = int(input()); m = int(input())
if n == 1:
    n = 2
data = []
vital = 0
for i in range(n, m+1):
    for x in range(2, i):
        if i%x == 0:
            vital = 1
            break
    if vital == 0:
        data.append(i)
    vital = 0

a = print(-1) if data == [] else print(f"{sum(data)}\n{data[0]}")