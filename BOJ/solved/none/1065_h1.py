
def number(n):
    v = set()
    b = 0
    value = 0
    for i in range(1,n+1):
        i = list(map(int,str(i)))
        for x in range(len(i)):
            try:
                value = (i[x] - i[x+1])
                v.add(value)
            except IndexError:
                pass
            
        if len(v) <= 1:
            b += 1
        v = set()
    return b
            


count = number(1000)
print(count)

#비트시프트(2<<3정수), format
#1~99까지는 모두 한수이다
#123 -> 1, 2, 3 -> 3-2 = 1, 2-1 = 1 => 모두 1로 같으므로 한수