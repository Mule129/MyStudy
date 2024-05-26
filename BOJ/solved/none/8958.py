n = int(input())
data = ""

for i in range(n):
    sum = []
    data = list(input())
    count = 0
    value = 0
    for x in data:
        if x == "X":
            count = 0
            sum.append(count)
            
        else:
            count += 1
            sum.append(count)
            
    for x in sum:
        value += x
    print(value)

    #이중배열로 푸는 방법도 있음(ex : value[i][x])
