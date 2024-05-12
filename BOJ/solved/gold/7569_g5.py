import sys
from collections import deque

input = sys.stdin.readline
queue = deque()
arr = list()

m, n, h = map(int, input().split())

for _h in range(h):
    for _n in range(n):
        for _m in range(m):
            arr.append(list(map(int, input().split())))
            
