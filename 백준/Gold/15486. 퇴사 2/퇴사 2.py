import sys
input=sys.stdin.readline

N=int(input())
time=[0]*(N+2) # 1-based
price=[0]*(N+2)
for i in range(1,N+1):
    t,p=map(int,input().split())
    time[i]=t
    price[i]=p


dp=[0]*(N+2)
for curr_day in range(1,N+2):
    # skip
    dp[curr_day]=max(dp[curr_day],dp[curr_day-1])
    # try
    end_day=curr_day+time[curr_day]
    if end_day<=N+1:
        dp[end_day]=max(dp[end_day],dp[curr_day]+price[curr_day])

print(max(dp))