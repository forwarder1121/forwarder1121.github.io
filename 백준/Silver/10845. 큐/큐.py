import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
commands=[input().split() for _ in range(N)]
queue=deque()

for command in commands:
    cmd_type=command[0]
    if cmd_type=="push":
        queue.append(command[1])
    elif cmd_type=="pop":
        print(queue.popleft() if queue else -1)
    elif cmd_type=="size":
        print(len(queue))
    elif cmd_type=="empty":
        print(0 if queue else 1)
    elif cmd_type=="front":
        print(queue[0] if queue else -1)
    elif cmd_type=="back":
        print(queue[-1] if queue else -1)
    