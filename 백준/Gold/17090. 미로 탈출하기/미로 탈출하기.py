import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

N,M=map(int,input().split())
board=[input().strip() for _ in range(N)]
dir={"U":(-1,0),"D":(1,0),"L":(0,-1),"R":(0,1)}

# 0:미방문, 1:경로에 있음, 2:탈출 가능, 3:탈출 불가
DP=[[0]*M for _ in range(N)]

def P(x,y):
    # base-condition
    if not (0<=x<N and 0<=y<M):
        return 2
    if DP[x][y]==1:
        return 3
    if DP[x][y] in [2,3]:
        return DP[x][y]
    # do 
    DP[x][y]=1
    dx,dy=dir[board[x][y]]
    result=P(x+dx,y+dy)
    DP[x][y]=result
    return result

answer=0
for x in range(N):
    for y in range(M):
        if P(x,y)==2:
            answer+=1

print(answer)

