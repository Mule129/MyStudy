n = int(input())
value = list(map(int, input().split()))

even_list = []
odd_list = []
vital = True
for i in value:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
        
if len(even_list) > len(odd_list):
    vital = False
if abs(len(even_list) - len(odd_list)) > 1:
    vital = False
print(int(vital))