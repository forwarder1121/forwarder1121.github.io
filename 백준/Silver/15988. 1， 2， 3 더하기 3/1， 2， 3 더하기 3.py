import sys
input=sys.stdin.readline

T=int(input())
cases=[int(input()) for _ in range(T)]
MAX=max(cases)

dp=[0]*(MAX+1)

# init
dp[1]=1
dp[2]=2
dp[3]=4

# recursion
for x in range(4,MAX+1):
    dp[x]=(dp[x-1]+dp[x-2]+dp[x-3])%1000000009

for case in cases:
    print(dp[case])