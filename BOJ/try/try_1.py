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

for _n in range(n):
    dump = list(map(int, input().split()))
    arr_dfs.append(dump)
    arr_bfs.append(dump)
    for _m in range(m):
        if dump[_m] == 2:
            queue.append([_m, _n])

# deep 
def dfs(data):
    pass


def bfs():
    while True:
        if len(queue) == 0:
            print(0)
            return
        else:
            x, y = queue.popleft()
            for dx, dy in dxy:
                # print(y+dy, x+dx)
                if 0 <= x+dx < m and 0 <= y+dy < n:
                    if arr_bfs[y+dy][x+dx] == 0:
                        arr_bfs[y+dy][x+dx] = 1
                        queue.append([y+dy, x+dx])
                    elif arr_bfs[y+dy][x+dx] == 3:
                        print(1)
                        return


if __name__ == "__main__":
    bfs()
    for _n in range(n):
        print(*arr_bfs[_n])

