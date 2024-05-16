n = int(input())
data = input().split()

vital = 0
cnt = 0
for i in data:
    i = int(i)
    for x in range(1, i+1):
        if x == 1 or x == i:
            continue
        if i%x == 0:
            vital = 1
    if vital == 0 and i != 1:
        cnt += 1
    vital = 0
print(cnt)
"""
숏코딩 : 
input();print(sum(all(n%j for j in range(2,n))*n>1 for n in map(int,input().split())))

n = 4
print(all(n%j for j in range(2, n)))#all : 인수가 비어있거나, 참이면 참 반환
print((n%j for j in range(2, n)))"""
