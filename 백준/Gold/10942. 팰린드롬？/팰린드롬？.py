import sys
input=sys.stdin.readline

N=int(input())
A=[0]+list(map(int,input().split())) # 1-based
E=int(input())
queries=[list(map(int,input().split())) for _ in range(E)]

dp=[[False]*(N+1) for _ in range(N+1)] # 1-based

for i in range(1,N+1):
    dp[i][i]=True

for i in range(N):
    if A[i]==A[i+1]:
        dp[i][i+1]=True

for i in range(N,0,-1):
    for j in range(i+2,N+1):
        dp[i][j]=True if dp[i+1][j-1] and A[i]==A[j] else False

for s,e in queries:
    print(1 if dp[s][e] else 0)