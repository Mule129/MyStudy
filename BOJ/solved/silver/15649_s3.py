# n과 m 1
n, m = map(int, input().split())


def bt(data: str):
    if len(data) == m:
        for i in data:
            print(i, end=" ")
        print()
        return
    for i in range(1, n+1):
        if str(i) not in data:
            bt(data+str(i))
            

for i in range(1, n+1):
    bt(str(i))