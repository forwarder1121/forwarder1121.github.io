import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
targets=list(map(int,input().split()))

dq=deque(range(1,N+1))
cnt=0
for target in targets:
    pos=dq.index(target)
    right=pos
    left=len(dq)-right
    
    if right<left:
        dq.rotate(-right)
        cnt+=right
    else:
        dq.rotate(left)
        cnt+=left
    dq.popleft()

print(cnt)