import sys
input=sys.stdin.readline

N,M=map(int,input().split())

numbers=[0]+list(map(int,input().split())) # 1-based
cases=[tuple(map(int,input().split())) for _ in range(M)]

dp=[0]*(N+1)
dp[1]=numbers[1]

for x in range(2,N+1):
    dp[x]=dp[x-1]+numbers[x]

for case in cases:
    l,r=case
    print(dp[r]-dp[l-1])