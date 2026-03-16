import sys
input=sys.stdin.readline

N=int(input())

prices=[0]+list(map(int,input().split()))

dp=[0]*(N+1)
dp[1]=prices[1]

for x in range(2,N+1):
    for i in range(1,x+1):
        dp[x]=max(dp[x],dp[x-i]+prices[i])

print(dp[N])