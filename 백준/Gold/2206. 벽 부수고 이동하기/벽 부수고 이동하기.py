import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[list(map(int,input().strip())) for _ in range(N)]

dist=[[[-1]*2 for _ in range(M)] for _ in range(N)]
visited=[[[False]*2 for _ in range(M)] for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    queue=deque()
    queue.append((0,0,0))
    dist[0][0][0]=1
    visited[0][0][0]=True
    while queue:
        cx,cy,cb=queue.popleft()
        if cx==N-1 and cy==M-1:
            return dist[cx][cy][cb]
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<N and 0<=ny<M:
                # case 1 : road
                if graph[nx][ny]==0 and not visited[nx][ny][cb]:
                    dist[nx][ny][cb]=dist[cx][cy][cb]+1
                    queue.append((nx,ny,cb))
                    visited[nx][ny][cb]=True
                # case 2 : wall -> break if available
                elif graph[nx][ny]==1 and cb==0 and not visited[nx][ny][cb]:
                    dist[nx][ny][1]=dist[cx][cy][cb]+1
                    queue.append((nx,ny,1))
                    visited[nx][ny][cb]=1
    return -1       

print(bfs())

# 3d - bfs