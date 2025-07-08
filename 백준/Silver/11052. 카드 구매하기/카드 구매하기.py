import sys
N=int(input())
prices=[0]+list(map(int,input().split()))

dp=[0]*(N+1)

dp[0]=0
dp[1]=prices[1]

for i in range(N+1):
    for k in range(i+1):
        dp[i]=max(dp[i-k]+prices[k],dp[i])

print(dp[N])