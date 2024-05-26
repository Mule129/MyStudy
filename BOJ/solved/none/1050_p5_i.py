n, m = map(int, input().split())

matter = {}
recipe = {}

for i in range(n):
    dump_1, dump_2 = map(str, input().split())
    matter[dump_1] = int(dump_2)

for i in range(m):
    name, cont = map(str, input().split("="))
    recipe[name] = {}
    for j in cont.split("+"):
        dump_1, dump_2 = 0, 0
        try:
            dump_1 = int(j[:1])
            dump_2 = j[1:]
        except:
            dump_1 = int(j[:2])
            dump_2 = j[2:]
        if dump_2 in recipe[name].keys():
            recipe[name][dump_2] = str(int(recipe[name][dump_2]) + dump_1)
        else:
            recipe[name][dump_2] = str(dump_1)

mony = 0
t = 0

for i in range(len(recipe)):
    for j in recipe:
        if j == "LOVE":
            continue
        for k in recipe[j]:
            for p in matter:
                if k not in matter:
                    break
                if p == k:
                    t += int(matter[p]) * int(recipe[j][k])
                

                
        matter[j] = t
        t = 0


print(matter)
print(recipe)
    
try:
    for i in recipe["LOVE"]:
        for j in matter:
            if i == j:
                mony += int(recipe["LOVE"][i]) * int(matter[j])
except:
    mony = -1

if mony > 100000000:
    print(1000000001)
else:
    print(mony)