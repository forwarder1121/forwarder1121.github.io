import sys
from collections import deque
from copy import deepcopy
input=sys.stdin.readline

N,M,G,R=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]

targets=[]
for x in range(N):
    for y in range(M):
        if board[x][y]==2:
            targets.append((x,y))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

RED,GREEN,FLOWER=1,2,3
def simulate():
    time=[[-1]*M for _ in range(N)]
    color=[[0]*M for _ in range(N)]
    queue=deque()
    for x in range(N):
        for y in range(M):
            if board[x][y]==3:
                time[x][y]=0
                color[x][y]=RED
                queue.append((x,y))
            elif board[x][y]==4:
                time[x][y]=0
                color[x][y]=GREEN
                queue.append((x,y))

    flowers=0

    while queue:
        cx,cy=queue.popleft()
        if color[cx][cy]==FLOWER:
            continue
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not board[nx][ny]==0:
                    if time[nx][ny]==-1:
                        time[nx][ny]=time[cx][cy]+1
                        color[nx][ny]=color[cx][cy]
                        queue.append((nx,ny))
                    elif time[nx][ny]==time[cx][cy]+1 and color[nx][ny]!=color[cx][cy] and color[nx][ny]!=FLOWER:
                        color[nx][ny]=FLOWER
                        flowers+=1
    return flowers

def P(idx,r,g):
    # base-condition
    if r==R and g==G:
        return simulate()
    
    if idx==len(targets):
        return 0
    
    answer=0
    tx,ty=targets[idx]
    
    # noting
    answer=max(answer,P(idx+1,r,g))

    # red
    if r<R:
        board[tx][ty]=3
        answer=max(answer,P(idx+1,r+1,g))
        board[tx][ty]=2

    # green
    if g<G:
        board[tx][ty]=4
        answer=max(answer,P(idx+1,r,g+1))
        board[tx][ty]=2

    return answer

print(P(0,0,0))