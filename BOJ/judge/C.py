# contest/problem/1303/3

from collections import deque

n = int(input())  # y
m = int(input())  # x

arr = []
queue = deque()

pos = [(0, -1), (0, 1), (1, 0), (-1, 0)]

for i in range(n):
    arr.append(list(map(int, input().split())))
jump_power = int(input())

queue.append((0, 0))

color = arr[0][0]

def manhattan(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

while True:
    if len(queue) == 0:
        # print(*arr)
        if arr[n-1][m-1] == 3 or n == 1 and m == 1:  # 도착지점에 도달하였는가
            print("ALIVE")
        else:
            print("DEAD")
        break
    else:
        x, y = queue.popleft()
        for i in range(-jump_power, jump_power+1):  # 맨해튼 이하로 점프
            for j in range(-jump_power, jump_power+1):
                # print(x+i, y+j)
                if 0 <= x + i < m and 0 <= y  + j < n:  # array over 체크
                    if arr[y + j][x + i] == color and manhattan(x, y, x+i, y+j) <= jump_power:  # 갈 수 있는 길인지 체크
                        # print("manhatan: ", manhattan(x, y, x+i, y+j), jump_power, "pos: ", x, y, x+i, y+j )
                        arr[y + j][x + i] = 3  # 방문시 3 체크
                        queue.appendleft((x + i, y + j))  # 다음 위치를 queue에 추가