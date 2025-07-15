import sys
input=sys.stdin.readline

MOD=15746
N=int(input())

dp=[0]*(N+1) # 1-based

dp[1]=1
if N==1:
    print(1)
    sys.exit()
dp[2]=2
for i in range(3,N+1):
    dp[i]=(dp[i-1]+dp[i-2])%MOD

print(dp[N])