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
def P(depth,remain):
    ''' Return "Future" best maximum value within current state.'''
    # base-condition
    if depth==N:
        return 0
    best=-1
    # skip
    best=max(best,P(depth+1,remain))
    # pick up
    if remain>=weight[depth]:
        best=max(best,value[depth]+P(depth+1,remain-weight[depth]))
    
    return best

answer=P(0,K)
print(answer)