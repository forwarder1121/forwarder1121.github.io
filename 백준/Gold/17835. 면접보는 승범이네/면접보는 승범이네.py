import sys,math,heapq
input=sys.stdin.readline

# input
N,M,K=map(int,input().split())
graph=[[] for _ in range(N+1)] # 1-based
for _ in range(M):
    a,b,c=map(int,input().split())
    graph[b].append((a,c)) # reversed
starts=list(map(int,input().split()))

# multi-source Dijkstra
def multi_source_Dijkstra():
    dist=[math.inf]*(N+1)
    for start in starts:
        dist[start]=0
    
    pq=[]
    for start in starts:
        heapq.heappush(pq,(0,start))
    
    while pq:
        cur_cost,cur_node=heapq.heappop(pq)
        
        if cur_cost!=dist[cur_node]:
            continue

        for next_node, next_cost in graph[cur_node]:
            new_cost=dist[cur_node]+next_cost
            if new_cost<dist[next_node]:
                dist[next_node]=new_cost
                heapq.heappush(pq,(new_cost,next_node))
    
    return [0]+dist[1:]

results=multi_source_Dijkstra()
print(results.index(max(results)),max(results))