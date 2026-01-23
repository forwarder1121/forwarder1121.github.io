import sys,heapq,math
from collections import defaultdict
input=sys.stdin.readline

N,M,X=map(int,input().split())
roads=[list(map(int,input().split())) for _ in range(M)]

edges=defaultdict(list)
reversed_edges=defaultdict(list)
for u,v,cost in roads:
    edges[u].append((v,cost))
    reversed_edges[v].append((u,cost))
# O()
def dijkstra(start,graph)->int:
    dist=[math.inf]*(N+1) # 1-based
    dist[start]=0
    pq=[]
    heapq.heappush(pq,(0,start)) # (cost,node)
    while pq:
        cur_cost,cur_node=heapq.heappop(pq)
        if cur_cost>dist[cur_node]:
            continue
        for next_node, next_cost in graph[cur_node]:
            new_cost=cur_cost+next_cost
            if new_cost<dist[next_node]:
                dist[next_node]=new_cost
                heapq.heappush(pq,(new_cost,next_node))
    return dist


from_x=dijkstra(X,edges)
to_x=dijkstra(X,reversed_edges)

answer=0
for i in range(1,N+1):
    answer=max(answer,from_x[i]+to_x[i])
print(answer)