"""
2가 출발지 
-1은 장애물 
3까지 도착이 가능하다면 1을 출력
불가능하다면 0을 출력
두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다

##t1
6 4
0 2 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 3


##t2
5 5
0 2 0 0 0
0 -1 -1 0 0
0 0 0 0 0
-1 -1 -1 0 0 
3 0 0 0 0 

##t3
5 5
0 2 0 0 0
0 -1 -1 0 0
0 0 0 0 0
-1 -1 -1 0 0 
3 -1 0 0 0 
"""
import sys
from collections import deque

queue = deque()
input = sys.stdin.readline
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

m, n = map(int, input().split())


arr_dfs = []
arr_bfs = []
visite = [[0 for _ in range(m)] for _ in range(n)]

for _n in range(n):
    dump = list(map(int, input().split()))
    arr_dfs.append(dump)
    arr_bfs.append(dump)
    for _m in range(m):
        if dump[_m] == 2:
            queue.append([_m, _n])

# deep 
def dfs():
    while True:
        if len(queue) == 0:
            print(0)
            return
        else:
            y, x = queue.pop()
            for dx, dy in dxy:
                if 0 <= x+dx < m and 0 <= y + dy < n:
                    if arr_dfs[y+dy][x+dx] == 0:
                        arr_dfs[y+dy][x+dx] = 1
                        queue.append([y+dy, x+dx])
                    elif arr_dfs[y+dy][x+dx] == 3:
                        print(1)
                        return


def re_dfs(pos_x, pos_y):
    if not (0 <= pos_x < m and 0 <= pos_y < n):
        return 0
    elif arr_dfs[pos_y][pos_x] == 3:
        return 1
    elif arr_dfs[pos_y][pos_x] == -1 or visite[pos_y][pos_x] == 1:
        return 0
    
    visite[pos_y][pos_x] = 1
    # if arr_dfs[pos_x][pos_x] == 0:
    if (re_dfs(pos_x + 1, pos_y) or re_dfs(pos_x - 1, pos_y) or re_dfs(pos_x, pos_y + 1) or re_dfs(pos_x, pos_y - 1)):
        return 1
    else:
        return 0
    



def bfs():
    while True:
        if len(queue) == 0:
            print(0)
            return
        else:
            y, x = queue.popleft()
            for dx, dy in dxy:
                if 0 <= x+dx < m and 0 <= y+dy < n:
                    if arr_bfs[y+dy][x+dx] == 0:
                        arr_bfs[y+dy][x+dx] = 1
                        queue.append([y+dy, x+dx])
                    elif arr_bfs[y+dy][x+dx] == 3:
                        print(1)
                        return


if __name__ == "__main__":
    x, y = queue.pop()
    if re_dfs(x, y) == 1:
        print(1)
    else:
        print(-1)
    # for _n in range(n):
    #     print(*arr_bfs[_n])

