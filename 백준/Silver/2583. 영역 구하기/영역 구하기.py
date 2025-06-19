import sys
from collections import deque 
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]
results=[]

N,M,K=map(int,input().split())
graph=[[True]*M for _ in range(N)]
visited=[[False]*M for _ in range(N)]

for _ in range(K):
    y1,x1,y2,x2=map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            graph[i][j]=False


def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
    area=1
    while queue:
        cx,cy=queue.popleft()
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not visited[nx][ny] and graph[nx][ny]==True:
                    queue.append((nx,ny))
                    visited[nx][ny]=True
                    area+=1
    return area

for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j]==True:
            results.append(bfs(i,j))
            

results.sort()
print(len(results))
print(*results)