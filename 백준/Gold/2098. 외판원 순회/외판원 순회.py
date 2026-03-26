import sys,math
from functools import lru_cache
input=sys.stdin.readline

N=int(input())
W=[list(map(int,input().split())) for _ in range(N)]
start=0

@lru_cache(None)
def P(cur,mask):
    ''' Returns minimum cost left '''
    # base-condition
    if mask==(1<<N)-1:
        if W[cur][start]!=0:
            return W[cur][start]
        return math.inf
    best=math.inf
    for nxt in range(N):
        if W[cur][nxt]==0:
            continue
        if mask&(1<<nxt):
            continue
        best=min(best,W[cur][nxt]+P(nxt,mask|(1<<nxt)))
    return best

answer=P(start,1<<start)
print(answer)