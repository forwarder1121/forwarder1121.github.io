import sys,math
input=sys.stdin.readline

N,S=map(int,input().split())
arr=list(map(int,input().split()))

prefix=[0]*(N+1)
for i in range(1,N+1):
    prefix[i]=prefix[i-1]+arr[i-1]

best=math.inf
start=0
end=1
while end<=N:
    interval_sum=prefix[end]-prefix[start]
    if interval_sum>=S:
        best=min(best,end-start)
        start+=1
    else:
        end+=1


print(best if best is not math.inf else 0)