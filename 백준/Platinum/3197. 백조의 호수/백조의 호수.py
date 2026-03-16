import sys
from collections import deque
input=sys.stdin.readline

# input
R,C=map(int,input().split())
graph=[list(input().strip()) for _ in range(R)]
visited=[[False]*C for _ in range(R)]

# init
dx=[-1,1,0,0]
dy=[0,0,-1,1]

water_queue=deque()
swan_queue=deque()
next_swan_queue=deque()

swans=[]
for x in range(R):
    for y in range(C):
        if graph[x][y]=="L":
            swans.append((x,y))
        if graph[x][y] in ("L","."):
            water_queue.append((x,y))

(sx,sy),(tx,ty)=swans
swan_queue.append((sx,sy))
visited[sx][sy]=True

# functions
# layered multi-source BFS
def melt()->None:
    for _ in range(len(water_queue)):
        cx,cy=water_queue.popleft()
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<R and 0<=ny<C:
                if graph[nx][ny]=="X":
                    graph[nx][ny]="."
                    water_queue.append((nx,ny))

# frontier BFS    
def canMeet()->bool:
    while swan_queue:
        cx,cy=swan_queue.popleft()
        if (cx,cy)==(tx,ty):
            return True
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<R and 0<=ny<C:
                if not visited[nx][ny]:
                    visited[nx][ny]=True
                    if graph[nx][ny] in (".","L"):
                        swan_queue.append((nx,ny))
                    elif graph[nx][ny]=="X":
                        next_swan_queue.append((nx,ny))

    return False

# simulation
day=0
while True:
    if canMeet():
        print(day)
        break
    melt()
    swan_queue,next_swan_queue=next_swan_queue,deque()
    day+=1