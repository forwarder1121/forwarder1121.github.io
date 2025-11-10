from collections import deque
# BFS
def solution(graph):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    N=len(graph)
    M=len(graph[0])
    visited=[[False]*M for _ in range(N)]
    dist=[[0]*M for _ in range(N)]
    
    def bfs(x,y):
        queue=deque()
        queue.append((x,y))
        dist[x][y]=1
        while queue:
            cx,cy=queue.popleft() # bfs
            if cx==N-1 and cy==M-1:
                return dist[N-1][M-1]
            for i in range(4):
                nx=cx+dx[i]
                ny=cy+dy[i]
                if 0<=nx<N and 0<=ny<M:
                    if graph[nx][ny]==1 and not visited[nx][ny]:
                        visited[nx][ny]=True
                        dist[nx][ny]=dist[cx][cy]+1
                        queue.append((nx,ny))
                        
        return -1
    
    return bfs(0,0)