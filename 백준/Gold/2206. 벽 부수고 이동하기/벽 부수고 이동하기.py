import sys
from collections import deque
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# bfs - 3d

N,M=map(int,input().split())
graph=[list(map(int,input().strip())) for _ in range(N)]
dist = [[[ -1 for _ in range(2) ] for _ in range(M)] for _ in range(N)]



def bfs():
    queue=deque()
    queue.append((0,0,0))
    dist[0][0][0]=1
    while queue:
        cx,cy,cb=queue.popleft()

        # base case
        if cx==N-1 and cy==M-1:
            return dist[cx][cy][cb]

        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<N and 0<=ny<M:
                # next is 0
                if dist[nx][ny][cb]==-1 and graph[nx][ny]==0:
                    dist[nx][ny][cb]=dist[cx][cy][cb]+1
                    queue.append((nx,ny,cb))
                # next is 1 and broken is 0 -> break
                elif dist[nx][ny][1]==-1 and graph[nx][ny]==1 and cb==0:
                    dist[nx][ny][1]=dist[cx][cy][cb]+1
                    queue.append((nx,ny,1))
    return -1

print(bfs())

                
                
        