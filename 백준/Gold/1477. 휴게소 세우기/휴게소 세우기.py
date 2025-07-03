import sys,math
input=sys.stdin.readline

N,M,L=map(int,input().split())
stations=list(map(int,input().split()))
stations.extend([0,L])
stations.sort()

gaps=[]
for i in range(len(stations)-1):
    gaps.append(stations[i+1]-stations[i])

# parametric search
# [left, right)

left,right=1,max(gaps)
answer=right
while left<=right:
    mid=(left+right)//2
    needed=sum([math.ceil(gap/mid)-1 for gap in gaps])
    #print(needed)
    if needed<=M:
        answer=mid
        right=mid-1
    else:
        left=mid+1
    
print(answer)