from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def solution(graph):
    
    # INIT
    N=len(graph)
    M=len(graph[0])
    visited=[[False]*M for _ in range(N)]
    distance=[[-1]*M for _ in range(N)]
    
    
    # BFS
    queue=deque()
    queue.append((0,0))
    visited[0][0]=True
    distance[0][0]=1
    while queue:
        cx,cy=queue.popleft()
        # base-condition
        if cx==N-1 and cy==M-1:
            return distance[cx][cy]
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not visited[nx][ny] and graph[nx][ny]==1:
                    visited[nx][ny]=True
                    distance[nx][ny]=distance[cx][cy]+1
                    queue.append((nx,ny))
    return -1
