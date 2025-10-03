import sys
from collections import deque
input=sys.stdin.readline

# init 
R,C=map(int,input().split())
graph=[list(input().strip()) for _ in range(R)]
distance=[[-1]*C for _ in range(R)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# initial settings
water_q=deque()
swan_q=deque()
next_swan_q=deque()

swans=[]
for x in range(R):
    for y in range(C):
        if graph[x][y]!="X":
            water_q.append((x,y))
        if graph[x][y]=="L":
            swans.append((x,y))

(sx,sy),(tx,ty)=swans
swan_q.append((sx,sy))

visited=[[False]*C for _ in range(R)]
visited[sx][sy]=True

# frontier BFS
def canMeet()->bool:
    global swan_q, next_swan_q
    while swan_q:
        x,y=swan_q.popleft()
        if (x,y)==(tx,ty):
            return True
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<R and 0<=ny<C:
                if not visited[nx][ny]:
                    visited[nx][ny]=True
                    if graph[nx][ny] in (".","L"):
                        swan_q.append((nx,ny))
                    elif graph[nx][ny]=="X":
                        next_swan_q.append((nx,ny))
    return False

# multi-source BFS
def melt():
    for _ in range((len(water_q))):
        x,y=water_q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<R and 0<=ny<C:
                if graph[nx][ny]=="X":
                    graph[nx][ny]="."
                    water_q.append((nx,ny))

# simulation
day=0
while True:
    if canMeet():
        print(day)
        break
    melt()
    swan_q,next_swan_q=next_swan_q,deque()
    day+=1

    