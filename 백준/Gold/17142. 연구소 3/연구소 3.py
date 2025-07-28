import sys,math
from collections import deque
from itertools import combinations
input=sys.stdin.readline

N,M=map(int,input().split())
space=[list(map(int,input().split())) for _ in range(N)]

candidate_virus=[]
blank=0
for i in range(N):
    for j in range(N):
        if space[i][j]==2:
            candidate_virus.append((i,j))
        elif space[i][j]==0:
            blank+=1
if blank==0:
    print(0)
    sys.exit()            
dx=[-1,1,0,0]
dy=[0,0,-1,1]
answer=math.inf
for virus in combinations(candidate_virus,M):
    left=blank
    queue=deque()
    dist=[[-1]*N for _ in range(N)]
    for vx,vy in virus:
        dist[vx][vy]=0
        queue.append((vx,vy))
    while queue:
        cx,cy=queue.popleft()
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if space[nx][ny]!=1 and dist[nx][ny]==-1:
                    dist[nx][ny]=dist[cx][cy]+1
                    queue.append((nx,ny))
                    if space[nx][ny]==0:
                        left-=1
                        if left==0:
                            answer=min(answer,dist[nx][ny])

print(-1 if answer==math.inf else answer)
