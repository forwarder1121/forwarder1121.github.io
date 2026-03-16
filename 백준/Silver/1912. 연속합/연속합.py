import sys
input=sys.stdin.readline

N=int(input())
numbers=list(map(int,input().split()))

dp=[0]*N # 0-based

dp[0]=numbers[0]
for x in range(N):
    dp[x]=max(numbers[x],dp[x-1]+numbers[x])

print(max(dp))
