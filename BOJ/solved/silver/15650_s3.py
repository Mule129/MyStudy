# n과 m 2
n, m = map(int, input().split())


def bt(data: str):
    if len(data) == m:
        for i in data:
            print(i, end=" ")
        print()
        return
    for i in range(1, n+1):
        if str(i) not in data and i > int(data[len(data)-1]):
            bt(data+str(i))
            

for i in range(1, n+1):
    bt(str(i))