import sys
input=sys.stdin.readline

N=int(input())
numbers=list(map(int,input().split()))
numbers.sort()

# binary search

M=int(input())
targets=list(map(int,input().split()))
#print(targets)


# [left, right)
def binary_search(target):
    left=0
    right=N
    while left<right:
        mid=(left+right)//2
        # to right
        if numbers[mid]<target:
            left=mid+1
        # to left
        elif numbers[mid]>target:
            right=mid
        # match
        else:
            return 1
            
    return 0

for target in targets:
    print(binary_search(target))