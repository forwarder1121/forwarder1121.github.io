import sys
from collections import deque 
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[list(map(int,input().strip())) for _ in range(N)]
visited=[[False]*M for _ in range(N)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
    while queue:
        c_x,c_y=queue.popleft()
        for i in range(4):
            nx=c_x+dx[i]
            ny=c_y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not visited[nx][ny] and graph[nx][ny]>0:
                    queue.append((nx,ny))
                    visited[nx][ny]=True
                    graph[nx][ny]=graph[c_x][c_y]+1
                    

bfs(0,0)
print(graph[N-1][M-1])