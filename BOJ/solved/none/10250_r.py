from math import ceil

loop = int(input())

for i in range(loop):
    h, w, n = map(int, input().split())
    value_1 = n%h
    if value_1 == 0:
        value_1 = h
    value = ceil(n/h)
    if value < 10:
        value = "0"+str(value)
    print(str(value_1)+str(value))