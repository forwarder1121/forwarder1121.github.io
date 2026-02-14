import sys,math
input=sys.stdin.readline

N,K=map(int,input().split())
arr=list(map(int,input().split()))

prefix=[0]*(N+1)
for i in range(1,N+1):
    prefix[i]=prefix[i-1]+arr[i-1]

best=-math.inf
for i in range(N-K+1):
    interval_sum=prefix[i+K]-prefix[i]
    best=max(best,interval_sum)

print(best)
