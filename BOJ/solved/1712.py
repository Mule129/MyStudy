a, b, c = list(map(int, input().split()))

cnt = 0
dump_1 = a

if b >= c:
    cnt = -1

while cnt != -1:
    cnt = a+b/c
    dump_1 = a + b*cnt - c*cnt


print(cnt)