n, m = map(int, input().split())

cnt = 0
value = [[[False for _ in range(n)] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    i -= 1; j -= 1; k -= 1
    value[i][j][k] = True
    

for i in range(1, n-1):
    for j in range(1, n-1):
        for k in range(1, n-1):
            if value[i][j][k] and value[i+1][j][k] and value[i][j+1][k] and value[i][j][k+1]:
                if value[i-1][j][k] and value[i][j-1][k] and value[i][j][k-1]:
                    cnt += 1
print(cnt)