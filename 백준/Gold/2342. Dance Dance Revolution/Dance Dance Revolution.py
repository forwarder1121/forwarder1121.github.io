import sys,math
input=sys.stdin.readline

INF=math.inf
A=list(map(int,input().split()))
A=A[:-1]
N=len(A)

def cost(a,b):
    if a==0:
        return 2
    if a==b:
        return 1
    if abs(a-b)==2:
        return 4
    return 3

DP=[[[INF]*5 for _ in range(5)] for _ in range(N+1)]
DP[0][0][0]=0

for i in range(N):
    x=A[i]
    for L in range(5):
        for R in range(5):
            if DP[i][L][R]==INF:
                continue
            if x!=R:
                DP[i+1][x][R]=min(DP[i+1][x][R],DP[i][L][R]+cost(L,x))
            if x!=L:
                DP[i+1][L][x]=min(DP[i+1][L][x],DP[i][L][R]+cost(R,x))

answer=INF
for L in range(5):
    for R in range(5):
        answer=min(answer,DP[N][L][R])
print(answer)