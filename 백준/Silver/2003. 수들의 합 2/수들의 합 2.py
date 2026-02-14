import sys,math
input=sys.stdin.readline

N,M=map(int,input().split())
arr=list(map(int,input().split()))



start=0
window_sum=0
answer=0
for end in range(N):
    window_sum+=arr[end]
    
    while window_sum>=M:
        if window_sum==M:
            answer+=1
        window_sum-=arr[start]
        start+=1

print(answer)