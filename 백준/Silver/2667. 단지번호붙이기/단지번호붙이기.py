import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
graph=[list(map(int,input().strip())) for _ in range(N)]
visited=[[False]*N for _ in range(N)]
dx=[0,0,-1,1]
dy=[1,-1,0,0]
results=[]
def bfs(x,y):
    area=1
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
    while queue:
        cx,cy=queue.popleft()
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if not visited[nx][ny] and graph[nx][ny]==1:
                    queue.append((nx,ny))
                    visited[nx][ny]=True
                    area+=1

    return area

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j]==1:
            results.append(bfs(i,j))

results.sort()
print(len(results))
print(*results)