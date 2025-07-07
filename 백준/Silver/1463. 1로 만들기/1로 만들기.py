import sys
input=sys.stdin.readline

N=int(input())

dp=[0]*(N+1)
dp[1]=0
for x in range(2,N+1):
    best=dp[x-1]
    if x%3==0:
        best=min(dp[x//3],best)
    if x%2==0:
        best=min(dp[x//2],best)
    dp[x]=best+1

print(dp[N])