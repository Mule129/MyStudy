# import sys
# input, k = map(int, sys.stdin.readline().split())

# list = [i for i in range(1, input+1)]

# cnt, read = k, (k-1)
# end = 0
# while True:
#     if (list[read] != -1) and (cnt == k):
#         print(f"{list[read]}", end=", ")
#         list[read] = -1
#         cnt = 1
#         read += 1
#         end += 1
#     elif (list[read] != -1) and (cnt != k):
#         read += 1
#         cnt += 1
#     else:
#         read += 1
            
#     if read >= input:
#         read -= input
#     if end >= input:
#         break

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

queue = deque([i for i in range(1, n+1)])
k -= 1
print("<", end= "")
while True:
    queue.rotate(-k)
    if (len(queue)) <= 1:
        print(queue[0], end = ">")
        break
    print(queue[0], end = ", ")
    queue.popleft()