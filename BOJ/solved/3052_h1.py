data = []
for i in range(10):
    data.append(int(input())%42)
value = 0
for i in range(10):
    count = 0
    for x in range(i+1, 10):######중요오######
        if data[i]==data[x]:
            count += 1
    if count == 0:
        value += 1

print(value)

"""
data = []
for i in range(10):
    data.append(int(input())%42)

data = set(data)
print(len(data))
"""