import sys
from collections import deque
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    p=input().strip()
    n=int(input())
    s=input().strip()
    
    if n==0:
        dq=deque()
    else:
        dq=deque(s[1:-1].split(","))
    
    rev=False
    err=False
    for cmd in p:
        if cmd=="R":
            rev=not rev
        elif cmd=="D":
            if not dq:
                print("error")
                err=True
                break
            if not rev:
                dq.popleft()
            else:
                dq.pop()
    
    if err:
        continue
    if not err:
        if rev:
            dq.reverse()
    print("["+",".join(dq)+"]")
    