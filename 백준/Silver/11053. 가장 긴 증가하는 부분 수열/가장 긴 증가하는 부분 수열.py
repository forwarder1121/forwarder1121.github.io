import sys
input=sys.stdin.readline

N=int(input())
numbers=list(map(int,input().split()))

dp=[1]*N # 0-based

for x in range(N):
    for i in range(x):
        if numbers[i]<numbers[x]:
            dp[x]=max(dp[x],dp[i]+1)


print(max(dp))