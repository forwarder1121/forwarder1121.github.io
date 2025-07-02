import sys
input=sys.stdin.readline

M,N=map(int,input().split())
snack_length=list(map(int,input().split()))

# binary search
# [left, right)

left=1
right=max(snack_length)+1
answer=0
while left<right:
    mid=(left+right)//2
    count=sum(snack//mid for snack in snack_length)
    
    # to right
    if count>=M:
        answer=mid
        left=mid+1
    # to left
    else:
        right=mid

print(answer)