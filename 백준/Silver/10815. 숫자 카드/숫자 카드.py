import sys
input=sys.stdin.readline

N=int(input())
numbers=list(map(int,input().split()))
numbers.sort()

M=int(input())
targets=list(map(int,input().split()))

# binary search
# [left, right)

def binary_search(target):
    left,right=0,N
    while left<right:
        mid=(left+right)//2
        # to right
        if target>numbers[mid]:
            left=mid+1
        # to left
        elif target<numbers[mid]:
            right=mid
        # match
        else:
            return 1
    return 0

print(*[binary_search(target) for target in targets])