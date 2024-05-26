data = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
num = input()
value = []
for i in num:
    for j in range(len(data)):
        if i in data[j] : value.append(j+2)

print(value)

time = 0

for i in value:
    time += (i + 1)
print(time)
