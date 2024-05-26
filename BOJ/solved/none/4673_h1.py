"""1 2 3 2 5 2 7 2 9 11 20 11 31 11 42 11 53 11 64 11 75 11 86 11 97 11 108 205 108"
192 193 204 


def number(n):
    n_ = 0
    value = []
    n_len = list(map(int,str(n)))
    if len(n_len) == 1:
        n_ = n + 2
        value = list(map(int, str(n+2)))
        if len(value) == 2:
            n_ = n + 11
            value = list(map(int, str(n+11)))
        
    elif len(n_len) >= 2:
        n_ = n + 11

    return n_
i = 1
while i <= 10000:
    print(i)
    i = number(i)
"""
def selfn(n):
    list_n = list(map(int,str(n)))
    
    return n + sum([i for i in list_n])

if __name__ == "__main__":
    list_b = []
    for i in range(10001):
        list_b.append(i)
    for i in range(10001):
        try:
            list_b.remove(selfn(i))
        except:
            pass
    for i in list_b:
        print(i)

