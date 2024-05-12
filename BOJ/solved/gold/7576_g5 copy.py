from collections import deque

import sys
input = sys.stdin.readline 

queue = deque()  # queue 선언

m, n = map(int, input().split())  # m, n 값을 입력받음
# m이 가로, n은 세로(m, n) = (x, y)
# visit = [[0 for _ in range(m)] for _ in range(n)] # 0은 방문 안함이라는 뜻 

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 동서남북 방향 선언

# input list
datamap = list()
for i in range(n):
    datamap.append(list(map(int, input().split())))

# 시작 위치 탐색 및 queue에 추가
for i in range(n):
    for j in range(m):
        if datamap[i][j] == 1:
            queue.append([j, i])


# queue에 유효한 값이 있다면 너비우선탐색 실행
while True:
    # queue에 유효한 값이 없다면 탐색 종료
    if len(queue) == 0:
        sad_tomato = False
        max_day = -1
        for i in range(n):
            for j in range(m):
                if datamap[i][j] == 0 or sad_tomato == True:
                    sad_tomato = True
                    break
                if max_day < datamap[i][j]:
                    max_day = datamap[i][j]
        
        # for i in range(n):
        #     for j in range(m):
        #         print(datamap[i][j], end=" ")
        #     print()
        if sad_tomato:
            print(-1)
        else:
            print(max_day-1)  # -1. 이미 한개의 익은 토마토가 존재하기 때문에
        break
    # queue에 유효한 값이 있다면, 그 위치를 탐색
    else:
        x, y = queue.popleft()
        # visit[y][x] = 1

        for dx, dy in dxy:
            if 0 <= x + dx < m and 0 <= y + dy < n:
                # if visit[y+dy][x+dx] == 0 and datamap[y+dy][x+dx] != -1:
                if datamap[y+dy][x+dx] == 0:
                    datamap[y+dy][x+dx] = datamap[y][x] + 1
                    queue.append((x+dx, y+dy))