import sys
input=sys.stdin.readline

N,M=map(int,input().split())
arr=list(map(int,input().split()))

prefix=[0]*N

for i in range(N):
    prefix[i]=prefix[i-1]+arr[i]

answer=[]
for _ in range(M):
    i,j=map(int,input().split())
    i_idx,j_idx=i-1,j-1
    result=prefix[j_idx]-prefix[i_idx]+arr[i_idx]
    answer.append(result)

print(*answer)