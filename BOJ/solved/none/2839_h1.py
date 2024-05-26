n = int(input())
data = 0
for i in range(n):
    data = n - (3 * i)
    if data%5 == 0:
        print(int(i + data/5))
        break
    elif data > n or data < 0:
        print(-1)
        break

"""
n=int(input())
print(-(n in[4,7])or n-2*n//5*2) #<-wow
"""