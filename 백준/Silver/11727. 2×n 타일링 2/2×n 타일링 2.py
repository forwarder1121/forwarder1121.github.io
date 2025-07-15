import sys
input=sys.stdin.readline


MOD = 10007
N=int(input())
if N==1:
    print(1)
    sys.exit()

dp=[0]*(N+1) # 1-based

dp[1]=1
dp[2]=3

for i in range(3,N+1):
    dp[i]=(dp[i-1]+2*dp[i-2])%MOD


print(dp[N])