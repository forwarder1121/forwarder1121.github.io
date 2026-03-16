import sys
input=sys.stdin.readline

N=int(input())
numbers=list(map(int,input().split()))

dp=[0]*N
for x in range(N):
    dp[x]=numbers[x]
    for i in range(x):
        if numbers[i]<numbers[x]:
            dp[x]=max(dp[x],dp[i]+numbers[x])

print(max(dp))