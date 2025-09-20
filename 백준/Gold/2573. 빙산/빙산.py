import sys
from collections import deque
input=sys.stdin.readline

# init
N,M=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# functions
def melt() -> bool:
    isMelted=False
    diff=[[0]*M for _ in range(N)]
    for cx in range(N):
        for cy in range(M):
            if graph[cx][cy]>0:
                for i in range(4):
                    nx=cx+dx[i]
                    ny=cy+dy[i]
                    if 0<=nx<N and 0<=ny<M:
                        if graph[nx][ny]==0:
                            diff[cx][cy]+=1
                            isMelted=True
    for x in range(N):
        for y in range(M):
            graph[x][y]=max(0,graph[x][y]-diff[x][y])
    return isMelted

def get_connected_components()->int:
    visited=[[False]*M for _ in range(N)]

    def bfs(x,y):
        queue=deque()
        queue.append((x,y))
        visited[x][y]=True
        while queue:
            cx,cy=queue.popleft()
            for i in range(4):
                nx=cx+dx[i]
                ny=cy+dy[i]
                if 0<=nx<N and 0<=ny<M:
                    if graph[nx][ny]>0 and not visited[nx][ny]:
                        queue.append((nx,ny))
                        visited[nx][ny]=True

    cp=0
    for x in range(N):
        for y in range(M):
            if graph[x][y]>0 and not visited[x][y]:
                bfs(x,y)
                cp+=1
    return cp



# main logic
day=0
while True:
    connected_components=get_connected_components()
    if connected_components>=2:
        print(day)
        break
    if not melt():
        print(0)
        break
    day+=1