def solution(N, edges):
    
    # INIT
    visited=[False]*N
    
    def dfs(u):
        visited[u]=True
        for v in range(N):
            if edges[u][v] and not visited[v]:
                dfs(v)
    
    count=0
    for i in range(N):
        if not visited[i]:
            count+=1
            dfs(i)
    
    return count