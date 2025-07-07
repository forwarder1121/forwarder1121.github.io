import sys
input=sys.stdin.readline

N=int(input())
snows=list(map(int,input().split()))

results=[]
for i in range(len(snows)):
    for j in range(i+1, len(snows)):
        results.append((snows[i]+snows[j],i,j))
results.sort()

import math
min_diff=math.inf
for i in range(len(results)-1):
    s1,l1,h1=results[i]
    s2,l2,h2=results[i+1]
    if l1!=l2 and l1!=h2 and h1!=l2 and h1!=h2:
        min_diff=min(min_diff,s2-s1)

print(min_diff)