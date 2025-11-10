# connected-component
def solution(N, computers):
    visited=[False]*N # 0-based
    count=0
    def dfs(u):
        for v in range(N):
            if computers[u][v]==1 and not visited[v]:
                visited[v]=True
                dfs(v)
                
    for i in range(N):
        if visited[i]==False:
            dfs(i)
            count+=1
    return count