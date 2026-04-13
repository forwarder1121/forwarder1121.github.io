import sys,math
input=sys.stdin.readline

INF=math.inf
C,N=map(int,input().split())
items=[list(map(int,input().split())) for _ in range(N)]

dp=[INF]*(C+101)
dp[0]=0
for cost,value in items:
    for x in range(value,C+101):
        dp[x]=min(dp[x],dp[x-value]+cost)

answer=min(dp[C:])
print(answer)