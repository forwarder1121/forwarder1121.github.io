import sys
input=sys.stdin.readline

# INPUT
N,M=map(int,input().split())
numbers=list(map(int,input().split()))
quires=[list(map(int,input().split())) for _ in range(M)]


# PROPRECESSING
prefix=[0]*(N+1)
for x in range(N):
    prefix[x+1]=prefix[x]+numbers[x]

answer=[]
for i,j in quires:
    result=prefix[j]-prefix[i-1]
    answer.append(result)
print(*answer)