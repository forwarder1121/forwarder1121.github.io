import math,heapq
from collections import defaultdict
def solution(N, paths, gates, summits):
    
    # GRAPH : graph[u]=(v,cost)
    graph=defaultdict(list)
    for i,j,w in paths:
        graph[i].append((j,w))
        graph[j].append((i,w))
        
    intensity=[math.inf]*(N+1) # 1-based
    
    pq=[] # PQ : (cost,node)
    
    gates=set(gates)
    summits=set(summits)
    
    # Multi-source
    for start in gates:
        intensity[start]=0
        heapq.heappush(pq,(0,start))
    
    while pq:
        cur_cost,cur_node=heapq.heappop(pq)
        if cur_cost>intensity[cur_node]:
            continue
        if cur_node in summits:
            continue
        for next_node, next_cost in graph[cur_node]:
            
            new_cost=max(next_cost,cur_cost)
            if new_cost<intensity[next_node]:
                intensity[next_node]=new_cost
                heapq.heappush(pq,(new_cost,next_node))
        
    # intensity[] has intensity to index
    min_summit=-1
    min_intensity=math.inf
    for end in sorted(summits):
        if min_intensity>intensity[end]:
            min_intensity=intensity[end]
            min_summit=end
    
    return min_summit,min_intensity