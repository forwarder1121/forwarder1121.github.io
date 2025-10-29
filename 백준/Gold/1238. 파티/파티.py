import sys,math,heapq
input=sys.stdin.readline

# input
N,M,X=map(int,input().split())
graph=[[] for _ in range(N+1)] # 1-based
for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

# dijkstra
def dijkstra(start,end)->int:
    dist=[math.inf]*(N+1)
    dist[start]=0

    pq=[]
    heapq.heappush(pq,(0,start))

    while pq:
        cur_cost,cur_node=heapq.heappop(pq)

        if cur_cost!=dist[cur_node]:
            continue

        for next_node, cost in graph[cur_node]:
            new_cost=dist[cur_node]+cost
            if new_cost<dist[next_node]:
                dist[next_node]=new_cost
                heapq.heappush(pq,(new_cost,next_node))

    return dist[end]

# result    
results=[]
for student in range(1,N+1):
    results.append(dijkstra(student,X)+dijkstra(X,student))
print(max(results))