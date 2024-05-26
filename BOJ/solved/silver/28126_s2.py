n = int(input())
command = input()
k = int(input())

x, y, z = 0, 0, 0

for i in command:
    if i == "U":
        y += 1
    elif i == "R":
        x += 1
    elif i == "X":
        z += 1

cnt = 0

for _ in range(k):
    x_go, y_go = map(int, input().split())
    x_go -= 1; y_go -= 1
    z_go = min(x_go, y_go, z)
    x_go -= z_go; y_go -= z_go
    if x_go <= x and y_go <= y:
        cnt += 1

if cnt > k:
    print(k)
else:
    print(cnt)