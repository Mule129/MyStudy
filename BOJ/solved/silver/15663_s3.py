# n과 m 5
# list 값을 입력받아 순차적으로 반복문 시행
n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

data = []

def bt(data: str) -> None:
    if len(data) == m:
        for i in data:
            print(i, end=" ")
        print()
        return
    for i in arr:
        if str(i) not in data:
            bt(data+str(i))

for i in arr:
    bt(str(i))