import sys
import math
from collections import deque
input=sys.stdin.readline

# init
N=int(input())
graph=[list(map(int,input().split())) for _ in range(N)]
distance=[[[-1]*2 for _ in range(N)] for _ in range(N)] # (distance, nation_num)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# logic flow
# 1. marking nation number
# 2. multi-source bfs
# 2-1. init bfs queue
# 2-2. bfs

# 1. marking nation number
nation_number=0
for x in range(N):
    for y in range(N):
        if graph[x][y]==1 and distance[x][y][0]==-1:
            nation_number+=1
            queue=deque()
            queue.append((x,y))
            distance[x][y][0]=0
            distance[x][y][1]=nation_number
            while queue:
                cx,cy=queue.popleft()
                for i in range(4):
                    nx=cx+dx[i]
                    ny=cy+dy[i]
                    if 0<=nx<N and 0<=ny<N:
                        if graph[nx][ny]==1 and distance[nx][ny][0]==-1:
                            queue.append((nx,ny))
                            distance[nx][ny][0]=0
                            distance[nx][ny][1]=nation_number

# 2. multi-source bfs
# 2-1. init bfs queue
queue=deque() # (x, y, nation_number)
for x in range(N):
    for y in range(N):
        if distance[x][y][0]==0:
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<N and 0<=ny<N:
                    if graph[nx][ny]==0:
                        queue.append((x,y,distance[x][y][1]))
                        break

# 2-2. bfs
min_length=math.inf               
while queue:
    cx,cy,cn=queue.popleft()
    for i in range(4):
        nx=cx+dx[i]
        ny=cy+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if not distance[nx][ny][0]==-1 and not distance[nx][ny][1]==cn:
                min_length=min(min_length,distance[nx][ny][0]+distance[cx][cy][0])
            if distance[nx][ny][0]==-1:
                queue.append((nx,ny,cn))
                distance[nx][ny][0]=distance[cx][cy][0]+1
                distance[nx][ny][1]=cn

print(min_length)
