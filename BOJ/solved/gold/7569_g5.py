import sys
from collections import deque

input = sys.stdin.readline
queue = deque()
arr = list()

m, n, h = map(int, input().split())
pos = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

# 3차원 데이터 input
dump = list()
for _h in range(h):
    for _n in range(n):
        dump.append(list(map(int, input().split())))
    arr.append(dump)
    dump = []


# start pos setting
for _h in range(h):
    for _n in range(n):
        for _m in range(m):
            if arr[_h][_n][_m] == 1:
                queue.append([_m, _n, _h])

# queue len size check
while True:
    if len(queue) == 0:
        max_day = -1
        sad_tomato = False

        for _h in range(h):
            for _n in range(n):
                for _m in range(m):
                    if arr[_h][_n][_m] == 0:
                        sad_tomato = True
                        break
                    if max_day < arr[_h][_n][_m]:
                        max_day = arr[_h][_n][_m]
                if sad_tomato:
                    break
            if sad_tomato:
                break

        if sad_tomato:
            print(-1)
        else:
            print(max_day-1)

        # print("===print result arr===")
        # for _h in range(h):
        #     for _n in range(n):
        #         print(*arr[_h][_n])
        break

    # add treu pos for queue
    else:
        x, y, z = queue.popleft()
        for dx, dy, dz in pos:
            if 0 <= x+dx < m and 0 <= y+dy < n and 0 <= z+dz < h:
                if arr[z+dz][y+dy][x+dx] == 0:
                    arr[z+dz][y+dy][x+dx] = arr[z][y][x] + 1
                    queue.append([x+dx, y+dy, z+dz])

                    
