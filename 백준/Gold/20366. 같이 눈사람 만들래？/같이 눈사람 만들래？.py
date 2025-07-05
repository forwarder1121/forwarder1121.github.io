import sys
input=sys.stdin.readline

N=int(input())
snows=list(map(int,input().split()))

# O(N^2)
results=[]
for i in range(len(snows)):
    for j in range(i+1,len(snows)):
        results.append((snows[i]+snows[j],i,j))

# sort => O(NlogN)
results.sort()
#print(results)
# O(N)
import math
min_diff=math.inf

for i in range(len(results)-1):
    s1,i1,j1=results[i]
    s2,i2,j2=results[i+1]
    if i1!=i2 and i1!=j2 and j1!=i2 and j1!=j2:
        min_diff=min(min_diff,s2-s1)
    
print(min_diff)

# total time complexity : O(N^2)