data = []
for i in range(3):
    data.append(int(input()))
data = list(str(data[0]*data[1]*data[2]))
data = list(map(int,data))

base = [0,0,0,0,0,0,0,0,0,0]
for i in data:
    #x = 0
    for x in range(10):
        if x == i:#list.count() 사용시 더 빠름
            base[x] = base[x] + 1
    #print(base[x])

for i in base:
    print(i)
