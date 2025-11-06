def solution(n, computers):
    visited=[False]*n
    answer=0
    
    def dfs(u):
        visited[u]=True
        for v in range(n):
            if computers[u][v]==1 and not visited[v]:
                dfs(v)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer+=1
            
    return answer