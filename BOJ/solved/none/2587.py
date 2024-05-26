data = []
for i in range(5):
    data.append(int(input()))
data.sort()
print(int(sum(data)/5))
print(data[2])