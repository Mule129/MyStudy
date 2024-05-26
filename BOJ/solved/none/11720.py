n = int(input())
data = list(map(int, str(input())))

count = 0
for i in range(n):
    count += data[i]
    
print(count)