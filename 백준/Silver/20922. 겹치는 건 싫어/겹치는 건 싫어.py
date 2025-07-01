import sys
from collections import defaultdict

N,K=map(int,input().split())
numbers=list(map(int,input().split()))
history=defaultdict(int)
# two pointers
# [left,right)
left=right=0
max_length=0
while(right<N):
    #print("left  : ",left, " right : ",right)
    #print(history)
    #expand
    if history[numbers[right]]<K:
        history[numbers[right]]+=1
        right+=1
        max_length=max(max_length,right-left)
    #shrink
    else:
        history[numbers[left]]-=1
        left+=1

print(max_length)
