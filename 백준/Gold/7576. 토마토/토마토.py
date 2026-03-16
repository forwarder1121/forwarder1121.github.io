import sys
from collections import deque
input=sys.stdin.readline

M,N=map(int,input().split())
boxes=[list(map(int,input().split())) for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

queue=deque()
for i in range(N):
    for j in range(M):
        if boxes[i][j]==1:
            queue.append((i,j))

while queue:
    cx,cy=queue.popleft()
    for i in range(4):
        nx=cx+dx[i]
        ny=cy+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if boxes[nx][ny]==0:
                boxes[nx][ny]=boxes[cx][cy]+1
                queue.append((nx,ny))

for i in range(N):
    for j in range(M):
        if boxes[i][j]==0:
            print(-1)
            sys.exit()
print(max(map(max,boxes))-1)