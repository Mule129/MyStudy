a = int(input())

cnt = 0
for i in range(a+1):
    cnt += i
    if cnt >= a:
        if i%2 == 0:
            print(f"{i-(cnt-a)}/{(cnt-a)+1}")
        else:
            print(f"{(cnt-a)+1}/{i-(cnt-a)}")
        break