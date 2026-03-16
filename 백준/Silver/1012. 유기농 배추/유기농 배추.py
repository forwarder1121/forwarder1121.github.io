import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

T=int(input())
dx=[-1,1,0,0]
dy=[0,0,1,-1]
def dfs(x,y):
    visited[y][x]=True
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<M and 0<=ny<N:
            if not visited[ny][nx] and farm[ny][nx]==1: 
                dfs(nx,ny)

for _ in range(T):
    M,N,K=map(int,input().split())
    farm=[[0]*M for _ in range(N)]
    visited=[[False]*M for _ in range(N)]

    for _ in range(K):
        x,y=map(int,input().split())
        farm[y][x]=1
    
    count=0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and farm[i][j]==1:
                dfs(j,i)
                count+=1
    print(count)