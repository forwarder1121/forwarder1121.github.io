import sys
import math
from collections import deque
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# init
N=int(input())
graph=[list(map(int,input().split())) for _ in range(N)]
marking=[[-1]*N for _ in range(N)]

# marking
partion_number=0
for x in range(N):
    for y in range(N):
        if graph[x][y]==1 and marking[x][y]==-1:
            partion_number+=1
            queue=deque()
            queue.append((x,y))
            marking[x][y]=partion_number
            while queue:
                cx,cy=queue.popleft()
                for i in range(4):
                    nx=cx+dx[i]
                    ny=cy+dy[i]
                    if 0<=nx<N and 0<=ny<N:
                        if graph[nx][ny]==1 and marking[nx][ny]==-1:
                            marking[nx][ny]=partion_number
                            queue.append((nx,ny))
            

# multi-source bfs
queue=deque()
distance=[[-1]*N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if graph[x][y]==1:
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<N and 0<=ny<N:
                    if graph[nx][ny]==0 and distance[nx][ny]==-1:
                        queue.append((x,y))
                        distance[x][y]=0

min_length=math.inf
while queue:
    cx,cy=queue.popleft()
    cm=marking[cx][cy]
    for i in range(4):
        nx=cx+dx[i]
        ny=cy+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if not distance[nx][ny]==-1 and not cm==marking[nx][ny]:
                min_length=min(min_length,distance[nx][ny]+distance[cx][cy])
            if graph[nx][ny]==0 and distance[nx][ny]==-1:
                distance[nx][ny]=distance[cx][cy]+1
                marking[nx][ny]=cm
                queue.append((nx,ny))

print(min_length)