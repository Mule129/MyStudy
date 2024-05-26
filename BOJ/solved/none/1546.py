n =  int(input())
data = list(map(int,input().split()))
high = 0
for i in range(n):
    if data[i] >= high:
        high = data[i]

value = 0
for i in range(len(data)):
    data[i] = data[i]/high*100
    value += data[i]

print(value/len(data))
