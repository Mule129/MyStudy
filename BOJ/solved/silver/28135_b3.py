n = int(input())

vital = False
cnt = 0
for i in range(49, n+1):
    if vital == True:
        cnt+= 1
        vital = False
    for j in range(len(str(i))):
        if j+1 >= len(str(i)):
            break
        if str(i)[j] + str(i)[j+1] == "50":
            vital = True
            break
        
    
print(cnt+n)