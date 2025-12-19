import sys
input=sys.stdin.readline

# INIT
MOD=10007
N,K=map(int,input().split())

# DP
dp=[[0]*(i+1) for i in range(N+1)] # 1-based
dp[0][0]=1
for i in range(1,N+1):
    dp[i][0]=1
    dp[i][i]=1
    for j in range(1,i):
        dp[i][j]=(dp[i-1][j-1]+dp[i-1][j])%MOD

print(dp[N][K])