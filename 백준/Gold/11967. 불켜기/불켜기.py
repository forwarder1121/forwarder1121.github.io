import sys
from collections import deque, defaultdict
input=sys.stdin.readline

# init
N,M=map(int,input().split())
lighted=[[False]*N for _ in range(N)]
visited=[[False]*N for _ in range(N)]
touched=[[False]*N for _ in range(N)]
answer=0

switches=defaultdict(list)
for _ in range(M):
    x,y,a,b=map(int,input().split())
    switches[(x-1,y-1)].append((a-1,b-1))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# logic flow : bfs + simulation
queue=deque()
queue.append((0,0))
lighted[0][0]=True
answer+=1

while queue:
    cx,cy=queue.popleft()
    visited[cx][cy]=True
    
    # turn on all possible rooms
    for tx,ty in switches[(cx,cy)]:
        if not lighted[tx][ty]:
            lighted[tx][ty]=True
            answer+=1
            if touched[tx][ty] and not visited[tx][ty]:
                queue.append((tx,ty))
                visited[tx][ty]=True

    # bfs
    for i in range(4):
        nx=cx+dx[i]
        ny=cy+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if lighted[nx][ny]:
                if not visited[nx][ny]:
                    visited[nx][ny]=True
                    queue.append((nx,ny))
            else:
                touched[nx][ny]=True

print(answer)