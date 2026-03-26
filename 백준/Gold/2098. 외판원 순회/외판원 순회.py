import sys,math
from functools import lru_cache
input=sys.stdin.readline

N=int(input())
W=[list(map(int,input().split())) for _ in range(N)]

INF=math.inf

start=0
@lru_cache(None)
def P(cur,visit):
    ''' Returns minimum cost to end circular path '''
    # base
    if visit==(1<<N)-1:
        if W[cur][start]!=0:
            return W[cur][start]
        return INF
    
    best=INF
    
    for nxt in range(N):
        if W[cur][nxt]==0:
            continue
        if visit&(1<<nxt):
            continue
        best=min(best,P(nxt,visit|(1<<nxt))+W[cur][nxt])
    return best

answer=P(start,1<<start)
print(answer)