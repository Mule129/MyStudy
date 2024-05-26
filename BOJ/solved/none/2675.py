T = int(input())

value = []
for i in range(T):
    R, S = input().split()
    S = list(S)
    dump = ""
    for x in S:
        for r in range(int(R)):
            dump += x
    value.append(dump)    
for i in value:
    print(i)

#문자열끼리 곱셈이 가능하다는것을 깜빡하고있었다..