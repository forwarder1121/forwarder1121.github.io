import sys,math,heapq
input=sys.stdin.readline

# input
N,M=map(int,input().split())
edges=[list(map(int,input().split())) for _ in range(M)]

graph=[[] for _ in range(N+1)] # 1-based
for idx,(a,b) in enumerate(edges):
    graph[a].append((b,idx))
    graph[b].append((a,idx))

start,end=1,N

# dijkstra
def dijkstra():
    dist=[math.inf]*(N+1)
    dist[start]=0

    pq=[]
    heapq.heappush(pq,(0,start))

    while pq:
        cur_dist,cur_node=heapq.heappop(pq)
        if cur_dist!=dist[cur_node]:
            continue
        for next_node,idx in graph[cur_node]:
            mod=cur_dist%M
            wait=(idx-mod)%M
            new_dist=cur_dist+wait+1
            if new_dist<dist[next_node]:
                dist[next_node]=new_dist
                heapq.heappush(pq,(new_dist,next_node))

    return dist[end]

# logic
print(dijkstra())