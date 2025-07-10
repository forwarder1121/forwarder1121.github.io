import sys
input=sys.stdin.readline

N=int(input())

dp=[0]*(N+2) # 1-based
dp[1]=1
dp[2]=2

for x in range(3,N+1):
    dp[x]=(dp[x-1]+dp[x-2])%10007

print(dp[N])