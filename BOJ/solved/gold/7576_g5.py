from collections import deque

import sys
input = sys.stdin.readline 

queue = deque()  # queue 선언

m, n = map(int, input().split())  # m, n 값을 입력받음
# m이 가로, n은 세로(m, n) = (x, y)
visit = [[0 for _ in range(m)] for _ in range(n)] # 0은 방문 안함이라는 뜻 

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 동서남북 방향 선언

# input list
datamap = list()
for i in range(n):
    datamap.append(list(map(int, input().split())))


# queue에 시작값 추가
for i in range(n):
    for j in range(m):
        if datamap[i][j] == 1:
            queue.appendleft((j, i)) # x y 

# 너비우선탐색 bfs
while True:
    # queue에 값이 없다면 == 더이상 탐색할 곳이 없다면
    if len(queue) == 0:
        zerodate = False  # zero 값이 있는지 없는지 여부 반환
        maxdate = -1  # 최대값 초기화(-1이상의 값이 나오기 때문에)

        # 최대 값 탐색
        for i in range(n):  # x
            for j in range(m):  # y
                if datamap[i][j] == 0:  # 0인 곳이 하나라도 있다면(익지 않은 토마토가 있다면)
                    zerodate = True
                maxdate = max((maxdate, datamap[i][j]))  # 날짜 반환
        if zerodate:  # 익지 않은 토마토가 있다면 -1 출력 후 종료
            print(-1)
            break
        else:
            print(maxdate - 1)  # max 날짜 반환
            # for i in range(n):
            #     print(*datamap[i])
            break
                
    else: # 큐가 비지않았다면 
        x, y = queue.pop()  # queue에서 값을 하나씩 출력(갈곳)
        visit[y][x] = 1  # 방문 기록

        for dx, dy in dxy:  # 상하좌우 탐색
            if 0 <= x + dx < m and 0 <= y + dy < n:  # array over 체크
                if visit[y+dy][x+dx] == 0 and datamap[y+dy][x+dx] != -1:  # 방문한 위치인지, 장애물이 있는지 체크
                    datamap[y+dy][x+dx] = datamap[y][x] + 1  # 기존 위치에 + 1 한 값을 상하좌우에 추가
                    queue.appendleft((x+dx, y+dy))  # 다음 위치를 queue에 추가