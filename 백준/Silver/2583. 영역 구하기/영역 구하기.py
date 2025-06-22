import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
M,N,K=map(int,input().split())
graph=[[0]*N for _ in range(M)]
visited=[[0]*N for _ in range(M)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(x,y):
    area=1
    visited[x][y]=True
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<M and 0<=ny<N:
            if not visited[nx][ny] and graph[nx][ny]==0:
                area+=dfs(nx,ny)
    return area

for _ in range(K):
    y1,x1,y2,x2=map(int,input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            graph[x][y]=1

results=[]
for i in range(M):
    for j in range(N):
        if not visited[i][j] and graph[i][j]==0:
            results.append(dfs(i,j))

results.sort()
print(len(results))
print(*results)