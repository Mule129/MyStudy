# contest/problem/1303/1

num_pos = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]

n = int(input())
for i in range(n):
    sum_arr = [0 for _ in range(3)]
    arr = list(map(int, input().split()))
    for index in arr:
        for j in range(3):
            sum_arr[j] = sum_arr[j] + num_pos[index][j]

    # print result
    cnt = 0
    for i in range(3):
        if sum_arr[i] == 2:
            cnt += 1
        elif sum_arr[i]%2 == 1:
            cnt += 100
    # print("sum_arr: ", *sum_arr)
    if cnt == 2:
        print("YES")
    else:
        print("NO")

