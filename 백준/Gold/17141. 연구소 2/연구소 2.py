import sys,copy,math
from collections import deque
from itertools import combinations
input=sys.stdin.readline

N,M=map(int,input().split())
space=[list(map(int,input().split())) for _ in range(N)]


candidate_virus=[]
blank=-M
for i in range(N):
    for j in range(N):
        if space[i][j]==2:
            blank+=1
            candidate_virus.append((i,j))
        elif space[i][j]==0:
            blank+=1

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 0 : empty, 1 : wall, 2 : virus
# insight : seperate "physical" and "theorical"
def bfs(viruses):
    dist=[[-1]*N for _ in range(N)]
    queue=deque()
    left=blank 
    if blank==0:
        return 0
    for vx,vy in viruses:
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
                    left-=1
                    if left==0:
                        return dist[nx][ny]
    return math.inf

answer=math.inf
for viruses in combinations(candidate_virus,M):
    answer=min(answer,bfs(viruses))


print(-1 if answer==math.inf else answer)