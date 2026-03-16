import sys
K,N=map(int,input().split())
lines=[int(input()) for _ in range(K)]

answer=0
# binary search
# [left, right)

left,right=1, max(lines)+1

while left<right:
    mid=(left+right)//2
    count=sum(line//mid for line in lines)
    # to right
    if count>=N:
        answer=mid
        left=mid+1
    # to left
    else:
        right=mid

print(answer)