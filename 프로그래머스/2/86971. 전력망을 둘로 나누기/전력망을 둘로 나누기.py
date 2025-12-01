from collections import defaultdict
import math
def solution(N, edges):
    
    # init graph
    graph=defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(deleted_edge,node_index,visited)->int:
        count=1
        visited[node_index]=True
        u,v=deleted_edge
        for next_node in graph[node_index]:
            if (u,v)==(node_index,next_node) or (v,u)==(node_index,next_node):
                continue
            if not visited[next_node]:
                count+=dfs(deleted_edge,next_node,visited)

        return count
    
    answer=math.inf
    
    for deleted_edge in edges:
        # cut edge
        # connected component
        visited=[False]*(N+1) # 1-based
        a=dfs(deleted_edge,1,visited)
        b=N-a
        diff=abs(a-b)
        answer=min(answer,diff)
        
    return answer


        
    
    
    
    
    