data = input()
base = ""
dump = ""
a = ""
b = ""
read = True
cnt = 0
while cnt < 2:
    
    for i in data.split("*"):
        cnt += 1
        if i == "*" and cnt == 0:
            read = True
        if read == True and i != " ":
            dump += i
            
    data = input()
    read = False
    if cnt == 1:
        a = dump
    else:
        b = dump

print("a: ", a, "b:", b)