import sys,math,heapq
input=sys.stdin.readline

# input
N,M=map(int,input().split())
edges=[list(map(int,input().split())) for _ in range(M)]
graph=[[] for _ in range(N+1)]

# 0-based
for i,(a,b) in enumerate(edges):
    graph[a].append((b,i))
    graph[b].append((a,i))

start,end=1,N

# dijkstra
def dijkstra():
    time=[math.inf]*(N+1) # 1-based
    time[start]=0

    pq=[]
    heapq.heappush(pq,(0,start))

    while pq:
        cur_time,cur_node=heapq.heappop(pq)
        if cur_time!=time[cur_node]:
            continue
        mod=cur_time%M
        for next_node, idx in graph[cur_node]:
            wait=(idx-mod)%M
            new_time=cur_time+wait+1
            if new_time<time[next_node]:
                time[next_node]=new_time
                heapq.heappush(pq,(new_time,next_node))

    return time[end]
            
print(dijkstra())