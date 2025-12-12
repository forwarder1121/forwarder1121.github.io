def solution(N, results):
    graph=[[False]*N for _ in range(N)] # 0-based
    
    for a,b in results:
        graph[a-1][b-1]=True
        
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][k] and graph[k][j]:
                    graph[i][j]=True
    answer = 0
    for i in range(N):
        known=sum(graph[i][j] or graph[j][i] for j in range(N))
        if known==N-1:
            answer+=1
    return answer