import sys
input=sys.stdin.readline

N,M=map(int,input().split())
A=list(map(int,input().split()))

diff=[0]*(N+1) # 0-based
for _ in range(M):
    a,b,k=map(int,input().split())
    diff[a-1]+=k
    diff[b]-=k

for x in range(1,N+1):
    diff[x]+=diff[x-1]

S=[0]*N
for i in range(N):
    S[i]=A[i]+diff[i]
print(*S)