n = 1
while True:
    n = int(input())
    if n == 0:
        break
    data = ((n*2)+1)*[True]#0~n*2까지
    
    for i in range(len(data)):
        
        if i < 2:
            data[i] = False
            continue
        
        if data[i] == True:
            for x in range(i+i, len(data), i):
                data[x] = False
                
    t = [i for i, x in enumerate(data) if x == True and i>n]
    print(len(t))
