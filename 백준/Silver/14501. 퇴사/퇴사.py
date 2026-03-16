import sys
input=sys.stdin.readline

N=int(input())

T=[0]*(N+2) # 1-based
P=[0]*(N+2)

for day in range(1,N+1):
    T[day],P[day]=map(int,input().split())


dp=[0]*(N+2)
for day in range(1,N+2):
    # skip
    dp[day]=max(dp[day],dp[day-1])
    # try
    if day+T[day]<=N+1:
        dp[day+T[day]]=max(dp[day+T[day]],dp[day]+P[day])

print(max(dp))