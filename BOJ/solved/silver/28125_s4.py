n = int(input())
string = []
cnt = 0
vital = True
for _ in range(n):
    string = list(input())
    for i in range(len(string)):
        if string[i] == "@":
            string[i] = "a"
            cnt += 1
        if string[i] == "[":
            string[i] = "c"
            cnt += 1
        if string[i] == "!":
            string[i] = "i"
            cnt += 1
        if string[i] == ";":
            string[i] = "j"
            cnt += 1
        if string[i] == "^":
            string[i] = "n"
            cnt += 1
        if string[i] == "0":
            string[i] = "o"
            cnt += 1
        if string[i] == "7":
            string[i] = "t"
            cnt += 1
        if string[i] == "\\":
            try:
                if string[i+1] == "'":
                    string[i] = "v"
                    string[i+1] = " "
                    cnt += 1
                    i = i+1
                elif string[i+1] == "\\" and string[i+2] == "'":
                    string[i] = "w"
                    string[i+1] = " "
                    string[i+2] = " "
                    cnt += 1
                    i = i+2
                    
            except:
                pass
    result = ""
    
    for i in string:
        if i == " ":
            pass
        else:
            result += i
            
    value_len = 0;    
    if len(result) % 2 == 1:
        value_len = len(result) + 1
    else:
        value_len = len(result)
    if len(result)/2 <= cnt:
        print("I don't understand")
    else:
        print(result)  
    cnt = 0