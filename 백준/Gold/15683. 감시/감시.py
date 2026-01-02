import sys,math
from itertools import permutations
from copy import deepcopy
input=sys.stdin.readline

N,M=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]

cctvs=[]
for x in range(N):
    for y in range(M):
        if 1<=board[x][y]<=5:
            cctvs.append((x,y,board[x][y]))

dx=[-1,0,1,0]
dy=[0,-1,0,1]

directions={
    1:[[0],[1],[2],[3]],
    2:[[0,2],[1,3]],
    3:[[0,1],[1,2],[2,3],[3,0]],
    4:[[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    5:[[0,1,2,3]]
}


def count_blind(board):
    return sum(row.count(0) for row in board)

def watch(board,x,y,direction):
    for d in direction:
        nx,ny=x,y
        while True:
            nx+=dx[d]
            ny+=dy[d]
            if not (0<=nx<N and 0<=ny<M):
                break
            if board[nx][ny]==6:
                break
            if board[nx][ny]==0:
                board[nx][ny]=-1

def dfs(level,board):
    # base-condition
    if level==len(cctvs):
        return count_blind(board)

    x,y,ctype=cctvs[level]
    best=math.inf

    for direction in directions[ctype]:
        newboard=deepcopy(board)
        watch(newboard,x,y,direction)
        best=min(best,dfs(level+1,newboard))
    
    return best

print(dfs(0,board))