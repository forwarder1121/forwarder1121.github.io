import sys,math
from copy import deepcopy
input=sys.stdin.readline

# INPUT
N,M=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

type2directions={
    1:[[0],[1],[2],[3]],
    2:[[0,2],[1,3]],
    3:[[0,1],[1,2],[2,3],[3,0]],
    4:[[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    5:[[0,1,2,3]]
}

cctvs=[]
for x in range(N):
    for y in range(M):
        if 1<=board[x][y]<=5:
            cctvs.append((x,y,board[x][y]))

def dfs(level,board):
    # base-condition
    if level==len(cctvs):
        return sum(row.count(0) for row in board)
    
    best=math.inf
    # apply
    x,y,ctype=cctvs[level]
    for directions in type2directions[ctype]:
        new_board=deepcopy(board)
        for d in directions:
            nx=x
            ny=y
            while True:
                nx+=dx[d]
                ny+=dy[d]
                if not (0<=nx<N and 0<=ny<M):
                    break
                if new_board[nx][ny]==6:
                    break
                if new_board[nx][ny]==0:
                    new_board[nx][ny]=-1

        # dfs
        result=dfs(level+1,new_board)
        best=min(best,result)

        # undo -> replaced by deepcopy
    return best
print(dfs(0,board)),
