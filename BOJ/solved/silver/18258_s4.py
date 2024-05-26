import sys

cmd_cnt = int(input())

que_stack = 0
que_len = 0
que = []
for _ in range(cmd_cnt):
    dump = sys.stdin.readline().split()
    if len(dump) >= 2:
        cmd, value = dump[0], dump[1]
        value = int(value)
    else:
        cmd = dump[0]
    
    if cmd == "push":
        que.append(value)
        que_stack += 1
        que_len += 1
    elif cmd == "pop":
        if que_len > 0:
            sys.stdout.write(str(que[que_stack-que_len]) + "\n")
            
            que_len -= 1
        else:
            sys.stdout.write(str(-1) + "\n")
    elif cmd == "size":
        sys.stdout.write(str(que_len) + "\n")
    elif cmd == "empty":
        sys.stdout.write(str(0) + "\n") if que_len > 0 else sys.stdout.write(str(1) + "\n")
    elif cmd == "front":
        sys.stdout.write(str(que[que_stack-que_len]) + "\n") if que_len > 0 else sys.stdout.write(str(-1) + "\n")
    elif cmd == "back":
        sys.stdout.write(str(que[que_stack-1]) + "\n") if que_len > 0 else sys.stdout.write(str(-1) + "\n")