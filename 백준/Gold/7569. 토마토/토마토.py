import sys
from collections import deque

input=sys.stdin.readline
M,N,H=map(int,input().split())

# initation
graph=[[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
dist=[[[-1]*M for _ in range(N)] for _ in range(H)]
queue=deque()

for h in range(H):
    for x in range(N):
        for y in range(M):
            if graph[h][x][y]==1:
                queue.append((h,x,y))
                dist[h][x][y]=0
            
# logic - 3d bfs
dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dh=[0,0,0,0,-1,1]

while queue:
    ch,cx,cy=queue.popleft()
    for i in range(6):
        nh,nx,ny=ch+dh[i],cx+dx[i],cy+dy[i]
        if 0<=nh<H and 0<=nx<N and 0<=ny<M:
            if graph[nh][nx][ny]==0 and dist[nh][nx][ny]==-1:
                queue.append((nh,nx,ny))
                dist[nh][nx][ny]=dist[ch][cx][cy]+1

answer=0
for h in range(H):
    for x in range(N):
        for y in range(M):
            if graph[h][x][y]==0 and dist[h][x][y]==-1:
                print(-1)
                sys.exit()
            answer=max(answer,dist[h][x][y])

print(answer)