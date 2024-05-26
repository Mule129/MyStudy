# 2470 두 용액
import sys

input = sys.stdin.readline

size = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

index_head = 0
index_tail = len(arr) - 1
save_index = []

print(arr)

defulte = arr[index_head] + arr[index_tail]
save_index.append([index_head, index_tail])
while True:
    if abs(arr[index_head] + arr[index_tail]) < defulte:
        defulte = arr[index_head] + arr[index_tail]
        save_index.append([index_head, index_tail])
    if index_head == index_tail - 1:
        break
    if defulte <= 0:
        index_head += 1
    else:
        index_tail -= 1

# print(defulte)
print(arr[save_index[-1][0]], arr[save_index[-1][1]])