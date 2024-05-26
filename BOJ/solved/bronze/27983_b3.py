n = int(input())

value = [[0 for _ in range(n)] for _ in range(3)]

for i in range(3):
    value[i] = list(map(str, input().split()))

new = [[0 for _ in range(3)] for _ in range(n)]
for i in range(len(value)):
    for j in range(len(value[0])):
        new[j][i] = value[i][j]

vital = False       
for i in range(len(new)):
    for j in range(i):
        if abs(int(new[i][0]) - int(new[j][0])) <= (int(new[i][1]) + int(new[j][1])) and new[i][2] != new[j][2]:
            print("YES")
            if j < i :
                print(j+1, i+1)
            else:
                print(i+1, j+1)
            vital = True
            break
    if vital == True:
        break
if vital == False:
    print("NO")