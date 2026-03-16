import sys,copy
from itertools import combinations
input=sys.stdin.readline

N,M=map(int,input().split())
space=[list(map(int,input().split())) for _ in range(N)]

# 0 : empty, 1 : wall, 2: virus
empty_space=[]
virus=[]
for i in range(N):
    for j in range(M):
        if space[i][j]==0:
            empty_space.append((i,j))
        if space[i][j]==2:
            virus.append((i,j))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(cx,cy,board):
    for i in range(4):
        nx,ny=cx+dx[i],cy+dy[i]
        if 0<=nx<N and 0<=ny<M and board[nx][ny]==0:
            board[nx][ny]=2
            dfs(nx,ny,board)

def simulate(board):
    for vx,vy in virus:
        dfs(vx,vy,board)
    return sum(row.count(0) for row in board)

best=0
for walls in combinations(empty_space,3):
    tmp_space=copy.deepcopy(space)
    for wx,wy in walls:
        tmp_space[wx][wy]=1
    best=max(best,simulate(tmp_space))

print(best)