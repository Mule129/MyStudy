n = int(input())
dump = 0
cnt = 0
cntList = list(map(int, input().split()))
for i in range(len(cntList)):
    try:
        if cntList[i] >= cntList[i+1]:
            cnt += 1
    except:
        if cntList[i] >= cntList[0]:
            cnt += 1
        
print(cnt)