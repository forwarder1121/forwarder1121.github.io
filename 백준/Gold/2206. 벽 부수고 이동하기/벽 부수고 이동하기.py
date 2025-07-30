import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[list(map(int,input().strip())) for _ in range(N)]
dist=[[[0]*2 for _ in range(M)] for _ in range(N)]
# dist[x][y][0] : unbroke wall
# dist[x][y][1] : broke wall

dx=[-1,1,0,0]
dy=[0,0,-1,1]

dist[0][0][0]=1

queue=deque()
queue.append((0,0,0))

while queue:
    cx,cy,broken=queue.popleft()
    if cx==N-1 and cy==M-1:
        print(dist[cx][cy][broken])
        sys.exit()
    for i in range(4):
        nx=cx+dx[i]
        ny=cy+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if graph[nx][ny]==0 and dist[nx][ny][broken]==0:
                dist[nx][ny][broken]=dist[cx][cy][broken]+1
                queue.append((nx,ny,broken))
            elif graph[nx][ny]==1 and broken==0 and dist[nx][ny][broken]==0:
                dist[nx][ny][1]=dist[cx][cy][broken]+1
                queue.append((nx,ny,1))
print(-1)    