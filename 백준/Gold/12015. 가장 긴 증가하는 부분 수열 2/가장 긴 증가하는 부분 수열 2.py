import sys
from bisect import bisect_left
input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

tails=[] # minimum ending value for each LIS length
for x in A:
    idx=bisect_left(tails,x)
    if idx==len(tails):
        tails.append(x)
    else:
        tails[idx]=x

answer=len(tails)
print(answer)