import sys,math,heapq
input=sys.stdin.readline

# input
N,M,start,end,money=map(int,input().split())
graph=[[] for _ in range(N+1)] # 1-based
max_edge_weight=0
for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    if c>max_edge_weight:
        max_edge_weight=c

def dijkstra(limit)->bool:
    dist=[math.inf]*(N+1) # 1-based
    dist[start]=0

    pq=[]
    heapq.heappush(pq,(0,start))

    while pq:
        cur_cost,cur_node=heapq.heappop(pq)
        if cur_cost!=dist[cur_node]:
            continue
        for next_node, cost in graph[cur_node]:
            if cost>limit:
                continue
            new_cost=cost+dist[cur_node]
            if new_cost<dist[next_node]:
                dist[next_node]=new_cost
                heapq.heappush(pq,(new_cost,next_node))
    
    return dist[end]<=money

low,high=0,max_edge_weight
answer=-1
while low<=high:
    mid=(low+high)//2
    if dijkstra(mid):
        answer=mid
        high=mid-1
    else:
        low=mid+1
print(answer)    