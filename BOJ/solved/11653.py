n = int(input())

while True:
    for i in range(2, n+1):
        if n%i == 0:
            print(i)
            n = int(n/i)
            break
    if n == 1:
        break