import sys,math,heapq
input=sys.stdin.readline

# input
V,E=map(int,input().split())
start=int(input())
graph=[[] for _ in range(V+1)]
for _ in range(E):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))

def dijkstra(start,graph,N):
    dist=[math.inf]*(N+1)
    dist[start]=0

    pq=[]
    heapq.heappush(pq,(0,start))

    while pq:
        cur_cost,cur_node=heapq.heappop(pq)

        if cur_cost!=dist[cur_node]:
            continue
        
        for next_node,cost in graph[cur_node]:
            new_cost=dist[cur_node]+cost
            if new_cost<dist[next_node]:
                dist[next_node]=new_cost
                heapq.heappush(pq,(new_cost,next_node))

    return dist

results=dijkstra(start,graph,V)

for i in range(1,V+1):
    if results[i]==math.inf:
        print("INF")
    else:
        print(results[i])