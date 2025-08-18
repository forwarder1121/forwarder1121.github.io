import sys
from collections import deque
input=sys.stdin.readline

N,L=map(int,input().split())
arr=list(map(int,input().split()))

dq=deque() # (index, value)
result=[]
for idx,value in enumerate(arr):
    while dq and dq[-1][1]>value:
        dq.pop()
    dq.append((idx,value))
    if dq[0][0]<=idx-L:
        dq.popleft()
    result.append(dq[0][1])

print(*result)
    