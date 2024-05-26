# 11053_s2 
# 각자리에 해당하는 값을 노트(길이를 노트한다)
# e.g) [10, 20, 1, 100, 15, 21, 22] -> [1] -> [1, 2] -> [1, 2, 1] -> [1, 2, 1, 3] -> [1, 2, 1, 3, 2] -> [1, 2, 1, 3, 2, 3] -> [1, 2, 1, 3, 2, 3, 4]


size = int(input())

arr = list(map(int, input().split()))

check_arr = [0 for _ in range(size)]  # 이전 값까지의 최대 길이를 저장한다
index = 0

check_arr[0] = 1
index += 1

dump = 0

for i in range(1, size):
    # 이전 값에 자신을 더한다
    # 이전의 이전 값에 자신을 더한다 -> 조건에 따라
    # 이전의 이전의 이전 값에 자신을 더한다.. -> max를 찾는 과정. 이때 자신보다 작은 값이여야 한다는 조건이 있다.
    # 이렇게 되면 반복 횟수가 2중 for문이랑 비슷해지지 않나?
    
    # if arr[i-1] < arr[i]:
    #     check_arr[index] = check_arr[index-1] + 1
    #     index += 1
    # else:
    #     check_arr[index] = 1
    #     for j in range(index, 0, -1):
    #         if arr[j] < arr[i]:
    #             check_arr[index] = check_arr[j] + check_arr[index]
    #             break
    #     index += 1
    
    for j in range(index):
        if arr[i] > arr[j] and check_arr[j] > dump:
            dump = check_arr[j]
    check_arr[index] = dump + 1
    index += 1
    dump = 0

    # print("check_arr: ", *check_arr)

print(max(check_arr))
        
    