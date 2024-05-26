roof = input()
dump_2 = []
cnt = 0
vital = 0
after = ""
for i in range(int(roof)):
    dump_2 = []
    vital = 0
    dump_1 = input()
    for x in dump_1:
        #print(f"x : {x}")
        if x in dump_2 and x != after:
            vital = 1
            break
        else:
            dump_2.append(x)
        after = x   
    if vital != 1:
        cnt += 1
        after = ""
    #print(f"cnt : {cnt} vital : {vital}") 
    
        
print(cnt)