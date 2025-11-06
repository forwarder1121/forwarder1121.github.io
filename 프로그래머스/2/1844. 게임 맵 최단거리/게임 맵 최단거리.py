from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def solution(graph):
    N=len(graph)
    M=len(graph[0])
    dist=[[0]*M for _ in range(N)]
    
    
    queue=deque()
    queue.append((0,0))
    dist[0][0]=1
    
    while queue:
        cx,cy=queue.popleft()
        if cx==N-1 and cy==M-1:
            return dist[N-1][M-1]
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny]==1 and dist[nx][ny]==0:
                    dist[nx][ny]=dist[cx][cy]+1
                    queue.append((nx,ny))
        
    
    
    return -1 