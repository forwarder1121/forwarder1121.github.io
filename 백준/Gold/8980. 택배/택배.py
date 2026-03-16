import sys
from collections import defaultdict
input=sys.stdin.readline

N,C=map(int,input().split())
M=int(input())
record=[list(map(int,input().split())) for _ in range(M)]

record.sort(key=lambda x:x[1])

answer=0
remaining=[C]*N
for s,e,w in record:
    possible=min(remaining[i] for i in range(s,e))
    take=min(possible,w)
    
    for i in range(s,e):
        remaining[i]-=take
    answer+=take
print(answer)