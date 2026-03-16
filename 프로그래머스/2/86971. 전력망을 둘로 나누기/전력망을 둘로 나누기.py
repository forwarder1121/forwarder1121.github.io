from collections import defaultdict
import math
def solution(N, edges):
    
    # making graph
    graph=defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # return connected-component
    def dfs(cur_node,deleted_edge,visited)->int:
        u,v=deleted_edge
        visited[cur_node]=True
        count=1
        for next_node in graph[cur_node]:
            if (cur_node,next_node)==(u,v) or (next_node,cur_node)==(v,u):
                continue
            if not visited[next_node]:
                count+=dfs(next_node,deleted_edge,visited)
        return count
                
    answer=math.inf
    for deleted_edge in edges:
        visited=[False]*(N+1) # 1-based
        size_a=dfs(deleted_edge[0],deleted_edge,visited)
        size_b=N-size_a
        diff=abs(size_a-size_b)
        answer=min(answer,diff)
        
    
    return answer