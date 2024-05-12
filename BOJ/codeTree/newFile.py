n = int(input())

def bt(data):
    global n
    if "111" in data or "000" in data:
        return
    else:
        if len(data) == n:
            print(data)
        elif len(data) < n:
            bt(data + "0")
            bt(data + "1")

bt("")

