import sys
from functools import lru_cache
input=sys.stdin.readline

# INPUT
N,K=map(int,input().split())
weight=[]
value=[]

for _ in range(N):
    w,v=map(int,input().split())
    weight.append(w)
    value.append(v)

@lru_cache(None)
def P(depth, remain):
    ''' Return best sum(value) of the future choice '''
    # base
    if depth==N:
        return 0
    best=-1
    # skip
    best=max(best,P(depth+1,remain))
    # pick up
    if remain>=weight[depth]:
        best=max(best,P(depth+1,remain-weight[depth])+value[depth])
    return best

answer=P(0,K)
print(answer)