n = int(input())
string = input()

cnt = 0 
for i in range(int(len(string)/2)):
    if string[i] != string[len(string)-i-1]:
        cnt += 1
        
print(cnt)