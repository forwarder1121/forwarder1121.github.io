import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
graph=[list(map(int,input().split())) for _ in range(N)]

max_height=max(map(max,graph))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
max_count=0

def bfs(x,y,rain,visited):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
    while queue:
        cx,cy=queue.popleft()
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if not visited[nx][ny] and graph[nx][ny]>rain:
                    queue.append((nx,ny))
                    visited[nx][ny]=True
                    
    

for rain in range(max_height):
    visited=[[False]*N for _ in range(N)]
    count=0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j]>rain:
               bfs(i,j,rain,visited)
               count+=1
    max_count=max(max_count,count)

print(max_count)