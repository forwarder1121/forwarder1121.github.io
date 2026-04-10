import sys,heapq
input=sys.stdin.readline

N=int(input())
tasks=[tuple(map(int,input().split())) for _ in range(N)]

tasks.sort()

pq=[]
for d,w in tasks:
    heapq.heappush(pq,w)
    if len(pq)>d:
        heapq.heappop(pq)

answer=sum(pq)
print(answer)