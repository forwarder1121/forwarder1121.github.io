import sys
input=sys.stdin.readline

state=0

M=int(input())

for _ in range(M):
    cmd=input().split()
    if cmd[0]=="add":
        x=int(cmd[1])-1
        state|=(1<<x)
    elif cmd[0]=="remove":
        x=int(cmd[1])-1
        state&=~(1<<x)
    elif cmd[0]=="check":
        x=int(cmd[1])-1
        if state&(1<<x):
            print(1)
        else:
            print(0)
    elif cmd[0]=="toggle":
        x=int(cmd[1])-1
        state^=(1<<x)
    elif cmd[0]=="all":
        state=(1<<21)-1
    elif cmd[0]=="empty":
        state&=0
    