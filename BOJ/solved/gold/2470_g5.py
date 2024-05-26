# # 2470 두 용액
# import sys

# input = sys.stdin.readline

# size = int(input())

# arr = list(map(int, input().split()))
# arr.sort()

# default = arr[0] + arr[size-1]
# save = [arr[0], arr[size-1]]

# # 인덱스는 서로 같은 값을 가지면 안된다
# # 2중 반복문은 시간초과
# # 인덱싱 포인터 이용하면 경우의 조건이 3개가량 있다. -> 이걸 재귀함수화 시킬 수 있을 것 같은데
# #   a와 b를 비교하고 결과값 리턴
# for i in range(size):
#     for j in range(size):
#         if abs(arr[i] + arr[j]) < abs(default) and i != j:
#             default = arr[i] + arr[j]
#             save = [arr[i], arr[j]]

# print(*save)


# 2470 두 용액
import sys

input = sys.stdin.readline

size = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

index_head = 0
index_tail = len(arr) - 1
save_index = []

defulte = arr[index_head] + arr[index_tail]
save_index.append([index_head, index_tail])
while True:
    if abs(arr[index_head] + arr[index_tail]) < abs(defulte):
        defulte = arr[index_head] + arr[index_tail]
        save_index.append([index_head, index_tail])
    if index_head == index_tail - 1:
        break
    if arr[index_head] + arr[index_tail] <= 0:
        index_head += 1
    else:
        index_tail -= 1

# print(defulte)
print(arr[save_index[-1][0]], arr[save_index[-1][1]])