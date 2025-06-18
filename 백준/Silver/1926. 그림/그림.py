from collections import deque

N,M=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]
visited=[[False]*M for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

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
                if not visited[nx][ny] and graph[nx][ny]==1:
                    visited[nx][ny]=True
                    queue.append((nx,ny))
                    area+=1
    return area

count=0
max_area=0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j]==1:
            count+=1
            max_area=max(max_area,bfs(i,j))

print(count)
print(max_area)