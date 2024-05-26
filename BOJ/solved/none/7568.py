n = int(input())

a, b = [0 for i in range(n)], [0 for i in range(n)]
rank = [1 for i in range(n)]
for i in range(n):
    a[i], b[i] = map(int, input().split())
for i in range(n):
    for j in range(len(a)):
        try:
            if (a[i] < a[j]) and (b[i] < b[j]):
                rank[i] += 1
        except Exception:
            pass
print(*rank)