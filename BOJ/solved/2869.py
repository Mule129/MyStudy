from math import ceil

a, b, v = map(int, input().split())

v = v - b

t = a - b

v = v / t

print(int(ceil(v)))