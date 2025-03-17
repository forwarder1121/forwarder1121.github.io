import heapq
#input
pq=[]
N=int(input())
result=0
for i in range(N):
    start,end=tuple(map(int,input().split()))
    heapq.heappush(pq,(end,start))

#logic
time=0
while pq:
    end,start=heapq.heappop(pq)
    if(start<time): continue
    time=end
    result+=1

print(result)

#time complexity : O(NlogN)