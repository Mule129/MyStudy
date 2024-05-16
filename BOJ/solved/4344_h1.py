n = int(input())
data = []
result = []

for i in range(n):
    value = 0
    count = 0
    data.append(list(map(int,input().split())))

    for x in range(1,data[i][0]+1):
        value += data[i][x]
    value = value/data[i][0]

    for x in data[i]:
        if data[i][0] == x:
            continue
        if x > value:
            count += 1

    count = str(count/data[i][0]*100)
    
    count = round(float(count),3)
    value = "{:.3f}%".format(count)
    
    print(value)