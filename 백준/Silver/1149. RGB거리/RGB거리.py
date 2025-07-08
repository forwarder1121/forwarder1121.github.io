import sys
input=sys.stdin.readline

N=int(input())
prices=[[0]*3]+[list(map(int,input().split())) for _ in range(N)]

dp=[[0]*3 for _ in range(N+1)]

# init
dp[1][0]=prices[1][0]
dp[1][1]=prices[1][1]
dp[1][2]=prices[1][2]

for i in range(2,N+1):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+prices[i][0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+prices[i][1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+prices[i][2]



print(min(dp[N]))