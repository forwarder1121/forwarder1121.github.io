import sys
from collections import deque
input=sys.stdin.readline

# init
N,M=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,1,-1]

# logic flow 
# 1. simulate melting
# 2. check connected component using bfs/dfs

def melt()->bool:
    diff=[[0]*M for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if graph[x][y]>0:
                for i in range(4):
                    nx=x+dx[i]
                    ny=y+dy[i]
                    if 0<=nx<N and 0<=ny<M:
                        if graph[nx][ny]==0:
                            diff[x][y]+=1
                            
    isMelted=False
    for x in range(N):
        for y in range(M):
            if graph[x][y] > 0: 
                new_h = max(0, graph[x][y] - diff[x][y])
                if new_h < graph[x][y]:
                    isMelted = True
                graph[x][y] = new_h    
    return isMelted

def get_connected_component()->int:
    visited=[[False]*M for _ in range(N)]
    cp=0

    def bfs(x,y)->None:
        queue=deque()
        queue.append((x,y))
        visited[x][y]=True
        while queue:
            cx,cy=queue.popleft()
            for i in range(4):
                nx=cx+dx[i]
                ny=cy+dy[i]
                if 0<=nx<N and 0<=ny<M:
                    if not visited[nx][ny] and graph[nx][ny]>0:
                        queue.append((nx,ny))
                        visited[nx][ny]=True
        

    for x in range(N):
        for y in range(M):
            if not visited[x][y] and graph[x][y]>0:
                bfs(x,y)
                cp+=1
    return cp

day=0                
while True:
    if get_connected_component()>=2:
        print(day)
        break
    if not melt():
        print(0)
        break
    day+=1
