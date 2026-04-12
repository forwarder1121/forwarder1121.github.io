import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
board=[list(map(int,input().strip())) for _ in range(N)]
visited=[[False]*M for _ in range(N)]
group_size={}
group_id=[[-1]*M for _ in range(N)]
gid=0

def BFS(x,y):
    global gid
    visited[x][y]=True
    group_id[x][y]=gid
    queue=deque()
    queue.append((x,y))
    size=0

    while queue:
        cx,cy=queue.popleft()
        size+=1
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx=cx+dx
            ny=cy+dy
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny]==0 and not visited[nx][ny]:
                    group_id[nx][ny]=gid
                    visited[nx][ny]=True
                    queue.append((nx,ny))
    
    group_size[gid]=size
    

# preprocessing
for x in range(N):
    for y in range(M):
        if board[x][y]==0 and not visited[x][y]:
            BFS(x,y) 
            gid+=1          

# calculate each wall
result=[[0]*M for _ in range(N)]
for x in range(N):
    for y in range(M):
        if board[x][y]==1:
            cnt=1
            seen=set()
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                nx=x+dx
                ny=y+dy
                if 0<=nx<N and 0<=ny<M:
                    if board[nx][ny]==0:
                        gid=group_id[nx][ny]
                        if gid not in seen:
                            cnt+=group_size[gid]
                            seen.add(gid)
            result[x][y]=cnt%10
                
# print answer
for row in result:
    print("".join(map(str,row)))

