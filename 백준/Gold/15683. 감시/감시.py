import sys
from copy import deepcopy
input=sys.stdin.readline

N,M=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]

cctvs=[]
for x in range(N):
    for y in range(M):
        if 1<=board[x][y]<=5:
            cctvs.append((board[x][y],x,y))

dx=[-1,0,1,0]
dy=[0,-1,0,1]

cctv2dirs={
    1:[[0],[1],[2],[3]],
    2:[[0,2],[1,3]],
    3:[[0,1],[1,2],[2,3],[3,0]],
    4:[[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    5:[[0,1,2,3]],
}

def P(idx,board):
    if idx==len(cctvs):
        return sum(row.count(1)+row.count(0) for row in board)
    answer=65
    ctype,cx,cy=cctvs[idx]
    for dirs in cctv2dirs[ctype]:
        new_board=deepcopy(board)
        new_board[cx][cy]=-1
        for dir in dirs:
            nx,ny=cx,cy
            while True:
                if not (0<=nx<N and 0<=ny<M):
                    break
                if new_board[nx][ny]==6:
                    break
                new_board[nx][ny]=-1
                nx+=dx[dir]
                ny+=dy[dir]
                
        answer=min(answer,P(idx+1,new_board))
    return answer

print(P(0,board))