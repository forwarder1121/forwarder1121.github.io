from collections import defaultdict
from collections import deque
def solution(N, edges):
    
    # INIT
    dist=[-1]*(N+1) # 1-based
    graph=defaultdict(list) 
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS
    queue=deque()
    queue.append(1)
    dist[1]=0
    
    while queue:
        cur_node=queue.popleft()
        for next_node in graph[cur_node]:            
            if dist[next_node]==-1:
                queue.append(next_node)
                dist[next_node]=dist[cur_node]+1
    
    max_dist=max(dist)
            
    return dist.count(max_dist)