import sys
from collections import deque
input=sys.stdin.readline

LEFT=list(input().strip())
RIGHT=[]
N=int(input())

for _ in range(N):
    cmd=input().split()
    if cmd[0]=="L":
        if LEFT:
            RIGHT.append(LEFT.pop())
    elif cmd[0]=="D":
        if RIGHT:
            LEFT.append(RIGHT.pop())
    elif cmd[0]=="P":
        LEFT.append(cmd[1])
    elif cmd[0]=="B":
        if LEFT:
            LEFT.pop()

answer="".join(LEFT)+"".join(reversed(RIGHT))
print(answer)
