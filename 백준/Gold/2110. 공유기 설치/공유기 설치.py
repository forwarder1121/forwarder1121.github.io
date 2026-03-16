import sys
input=sys.stdin.readline

N,C=map(int,input().split())
houses=sorted([int(input()) for _ in range(N)])

MAX=int(10e9)

def can(l):
    count=1
    prev=0
    for i in range(N):
        if houses[i]-houses[prev]>=l:
            count+=1
            prev=i
    return count>=C

left,right=0,MAX
answer=0
while left<=right:
    mid=(left+right)//2
    if can(mid):
        answer=mid
        left=mid+1
    else:
        right=mid-1

print(answer)

