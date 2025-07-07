import sys
input=sys.stdin.readline


T=int(input())

cases=[int(input()) for _ in range(T)]
N=max(cases)

dp=[0]*(N+1)
dp[1]=1
dp[2]=2
dp[3]=4
for x in range(4, N+1):
    dp[x]=dp[x-1]+dp[x-2]+dp[x-3]

for case in cases:
    print(dp[case])