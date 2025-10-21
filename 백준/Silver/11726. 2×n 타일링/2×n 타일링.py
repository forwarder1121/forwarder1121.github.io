import sys
input=sys.stdin.readline

N=int(input())

if N==1:
    print(1)
    sys.exit()

# DP
dp=[0]*(N+1) # 1-based
dp[1]=1
dp[2]=2

for i in range(3,N+1):
    dp[i]=(dp[i-1]+dp[i-2])%10007

print(dp[N])