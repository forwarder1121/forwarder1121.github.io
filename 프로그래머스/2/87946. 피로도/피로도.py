def solution(init_state, dungeons):
    
    N=len(dungeons)
    visited=[False]*N
    
    def dfs(state,count)->int:  
        best=count
        for i in range(N):
            if not visited[i] and state>=dungeons[i][0]:
                visited[i]=True
                best=max(best,dfs(state-dungeons[i][1],count+1))
                visited[i]=False
        return best
    
    answer=dfs(init_state,0)
    
    return answer