import sys
from collections import deque
input=sys.stdin.readline

R,C=map(int,input().split())
map=[input() for _ in range(R)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

fire_time=[[-1]*C for _ in range(R)]
jihoon_time=[[-1]*C for _ in range(R)]
fire_queue=deque()
jihoon_queue=deque()

for i in range(R):
    for j in range(C):
        if map[i][j]=="F":
            fire_time[i][j]=0
            fire_queue.append((i,j))
        if map[i][j]=="J":
            jihoon_time[i][j]=0
            jihoon_queue.append((i,j))



while fire_queue:
    cx,cy=fire_queue.popleft()
    for i in range(4):
        nx=cx+dx[i]
        ny=cy+dy[i]
        if 0<=nx<R and 0<=ny<C:
            if fire_time[nx][ny]==-1 and map[nx][ny]!="#":
                fire_time[nx][ny]=fire_time[cx][cy]+1
                fire_queue.append((nx,ny))

while jihoon_queue:
    cx,cy=jihoon_queue.popleft()

    if cx==0 or cx==R-1 or cy==0 or cy==C-1:
        print(jihoon_time[cx][cy]+1)
        sys.exit()

    for i in range(4):
        nx=cx+dx[i]
        ny=cy+dy[i]
        if 0<=nx<R and 0<=ny<C:
            if map[nx][ny]!="#" and jihoon_time[nx][ny]==-1:
                if fire_time[nx][ny]==-1 or jihoon_time[cx][cy]+1<fire_time[nx][ny]:
                    jihoon_time[nx][ny]=jihoon_time[cx][cy]+1
                    jihoon_queue.append((nx,ny))


print("IMPOSSIBLE")