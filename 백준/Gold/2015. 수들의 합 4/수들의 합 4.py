import sys
from collections import defaultdict
input=sys.stdin.readline

N,K=map(int,input().split())
arr=list(map(int,input().split()))

answer=0
freq=defaultdict(int)
freq[0]=1
prefix=0
for j in range(N):
    prefix+=arr[j]
    answer+=freq[prefix-K]
    freq[prefix]+=1
print(answer)