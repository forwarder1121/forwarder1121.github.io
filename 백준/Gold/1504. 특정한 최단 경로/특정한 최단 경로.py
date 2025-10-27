import sys,math,heapq
input=sys.stdin.readline

# input
V,E=map(int,input().split())
graph=[[] for _ in range(V+1)] # 1-based
for _ in range(E):
    a,b,weight=map(int,input().split())
    graph[a].append((b,weight))
    graph[b].append((a,weight))
v1,v2=map(int,input().split())

# Dijkstra
def dijkstra(start,end):
    dist=[math.inf]*(V+1)
    dist[start]=0

    pq=[]
    heapq.heappush(pq,(0,start))

    while pq:
        cur_cost,cur_node=heapq.heappop(pq)
        if cur_cost!=dist[cur_node]:
            continue
        for next_node, next_weight in graph[cur_node]:
            new_weight=dist[cur_node]+next_weight
            if new_weight<dist[next_node]:
                dist[next_node]=new_weight
                heapq.heappush(pq,(new_weight, next_node))   
    return dist[end]

# logic
result1=dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,V)
result2=dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,V)
result=min(result1,result2)

print(-1 if result==math.inf else result)
