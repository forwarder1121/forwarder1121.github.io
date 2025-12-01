def solution(k, dungeons):
    N=len(dungeons)
    visited=[False]*N
    
    def backtracking(energy)->int:
        max_count=0
        for i in range(N):
            req,cost=dungeons[i]
            if not visited[i] and energy>=req:
                visited[i]=True
                count=1+backtracking(energy-cost)
                max_count=max(max_count,count)
                visited[i]=False
                
        return max_count
        
    return  backtracking(k)


