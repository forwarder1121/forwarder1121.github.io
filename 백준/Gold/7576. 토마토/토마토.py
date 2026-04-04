import sys
from collections import deque
input=sys.stdin.readline

M,N=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]
visited=[[False]*M for _ in range(N)]

queue=deque()
remain=0
for x in range(N):
    for y in range(M):
        if board[x][y]==1:
            queue.append((x,y,0))
        if board[x][y]==0:
            remain+=1


max_dist=0
while queue:
    cx,cy,cdist=queue.popleft()
    max_dist=max(max_dist,cdist)
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx,ny=cx+dx,cy+dy
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny]==0:
                if not visited[nx][ny]:
                    queue.append((nx,ny,cdist+1))
                    visited[nx][ny]=True
                    remain-=1

if remain:
    print(-1)
else:
    print(max_dist)
