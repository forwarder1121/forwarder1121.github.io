import sys
from collections import deque
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        c_x,c_y=queue.popleft()
        for i in range(4):
            nx=c_x+dx[i]
            ny=c_y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not visited[nx][ny] and graph[nx][ny]==1:
                    queue.append((nx,ny))
                    visited[nx][ny]=True

T=int(input())
for _ in range(T):
    M,N,K=map(int,input().split())
    graph=[[0]*M for _ in range(N)]
    visited=[[False]*M for _ in range(N)]
    for _ in range(K):
        pos_y,pos_x=map(int,input().split())
        graph[pos_x][pos_y]=1

    connected_components=0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j]==1:
                bfs(i,j)
                connected_components+=1
    
    print(connected_components)
    

    