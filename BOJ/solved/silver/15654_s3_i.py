# n과 m 5
n, m = map(int, input().split())


def bt(data: str):
    if len(data) == m:
        for i in data:
            print(i, end=" ")
        print()
        return
    for i in range(1, n+1):
        if i >= int(data[len(data)-1]):
            bt(data+str(i))

for i in range(1, n+1):
    bt(str(i))