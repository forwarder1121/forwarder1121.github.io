import sys,heapq
input=sys.stdin.readline

N=int(input())
lines=[tuple(map(int,input().split())) for _ in range(N)]

pq=[]
for s,e in lines:
    heapq.heappush(pq,(e,s))

cur_time=0
answer=0
while pq:
    e,s=heapq.heappop(pq)
    if s<cur_time:
        continue
    cur_time=e
    answer+=1

print(answer)
