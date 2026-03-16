import sys,heapq
input=sys.stdin.readline

N=int(input())
lectures=[tuple(map(int,input().split())) for _ in range(N)]
lectures.sort()

heap=[]
for start,end in lectures:
    if heap and heap[0]<=start:
        heapq.heappop(heap)
    heapq.heappush(heap,end)

print(len(heap))
