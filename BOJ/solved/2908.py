a, b = input().split()

dump_a = int(a[2]+a[1]+a[0])
dump_b = int(b[2]+b[1]+b[0])
if dump_a > dump_b : print(dump_a)
else : print(dump_b)