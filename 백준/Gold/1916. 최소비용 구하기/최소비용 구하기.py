import sys,math,heapq
input=sys.stdin.readline

# input
N=int(input())
M=int(input())
graph=[[] for _ in range(N+1)] # 1-based
for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
start,end=map(int,input().split())

# Dijkstra
def dijkstra(start,end)->int:
    dist=[math.inf]*(N+1)
    dist[start]=0

    pq=[]
    heapq.heappush(pq,(0,start))

    while pq:
        cur_cost,cur_node=heapq.heappop(pq)
        
        if cur_cost!=dist[cur_node]:
            continue

        for next_node, next_cost in graph[cur_node]:
            new_cost=cur_cost+next_cost
            if new_cost<dist[next_node]:
                dist[next_node]=new_cost
                heapq.heappush(pq,(new_cost,next_node))
    return dist[end]

# logic
print(dijkstra(start,end))