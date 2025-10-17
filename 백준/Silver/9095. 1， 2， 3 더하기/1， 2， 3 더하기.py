import sys
input=sys.stdin.readline

# input
T=int(input())
taget_numbers=[int(input()) for _ in range(T)]
N=max(taget_numbers)


# DP
dp=[0]*(N+1) # 1-based
dp[1],dp[2],dp[3]=1,2,4

for i in range(4,N+1):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

# result
for target in taget_numbers:
    print(dp[target]) 