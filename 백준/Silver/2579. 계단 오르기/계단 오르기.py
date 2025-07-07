import sys
input=sys.stdin.readline

N=int(input())
scores=[0]+[int(input()) for _ in range(N)]

dp=[0]*(N+1)
dp[1]=scores[1]

if N>=2:
    dp[2]=dp[1]+scores[2]
if N>=3:
    dp[3]=max(dp[1],dp[2])+scores[3]

for x in range(3,len(scores)):
    dp[x]=max(dp[x-2],dp[x-3]+scores[x-1])+scores[x]

print(dp[N])