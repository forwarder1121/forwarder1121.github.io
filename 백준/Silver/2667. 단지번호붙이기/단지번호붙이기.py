import sys
input=sys.stdin.readline

N=int(input())
graph=[list(map(int,input().strip())) for _ in range(N)]
visited=[[False]*N for _ in range(N)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    area=1
    visited[x][y]=True
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if not visited[nx][ny] and graph[nx][ny]==1:
                area+=dfs(nx,ny)
    return area

results=[]
for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j]==1:
            results.append(dfs(i,j))

results.sort()
print(len(results))
print(*results)