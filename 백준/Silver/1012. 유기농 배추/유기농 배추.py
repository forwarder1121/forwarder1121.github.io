import sys
from collections import deque
input=sys.stdin.readline
T=int(input())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

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
                if not visited[nx][ny] and graph[nx][ny]==1:
                    queue.append((nx,ny))
                    visited[nx][ny]=True
                

for _ in range(T):
    N,M,K=map(int,input().split())
    graph=[[0]*M for _ in range(N)]
    visited=[[False]*M for _ in range(N)]
    for _ in range(K):
        x,y=map(int,input().split())
        graph[x][y]=1
    
    count=0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j]==1:
                bfs(i,j)
                count+=1
    print(count)

