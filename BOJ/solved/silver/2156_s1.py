import sys

"""
1. 지금 포도주를 마시지않는다
-> 나 이전의 최대값을 사용한다 (n-1최대값
2. 지금 포도주를 마신다. 
2-1 -> n-1은 안마시는걸로 따진다. 
n-2의 최대값 + 자기자신
2-2 -> n-2를 안마시는 걸로 따진다.
자기자신과 직전과 n-3의 최대값을 사용 
"""


input = sys.stdin.readline

n = int(input())

arr = []
sum_arr = [0] * n

index = 0

for i in range(n):
    arr.append(int(input()))

while index < n:
    if index == 0:
        sum_arr[index] = arr[index]
        index += 1
        continue
    elif index-1 == 0:
        sum_arr[index] = sum_arr[index-1] + arr[index]
        index += 1
        continue
    elif index-2 == 0:
        sum_arr[index] = max(sum_arr[index-2] + arr[index], sum_arr[index-1], arr[index] + arr[index-1])
        index += 1
        continue

    root_1 = sum_arr[index-1]  # 자기자신 x, n-1의 최대값 사용 
    root_2 = sum_arr[index-2] + arr[index]  # 자기자신과 n-2의 최대값 사용
    root_3 = sum_arr[index-3] + arr[index-1] + arr[index]  # 자기자신과 n-3의 최대값 사용
    
    sum_arr[index] = max(root_1, root_2, root_3)
    index += 1

    # print("sum: ", *sum_arr)/

    if index == len(arr):
        break

print(sum_arr[index-1])
