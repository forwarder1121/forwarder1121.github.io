import sys
from collections import deque
input=sys.stdin.readline

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(x,y):
    if x == x2 and y == y2:
        return 0
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
    while queue:
        cx,cy=queue.popleft()
        for i in range(8):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if not visited[nx][ny]:
                    visited[nx][ny]=True
                    graph[nx][ny]=graph[cx][cy]+1
                    queue.append((nx,ny))
                    if nx==x2 and ny==y2:
                        return graph[nx][ny]
                

T=int(input())
for _ in range(T):
    N=int(input())
    graph=[[0]*N for _ in range(N)]
    visited=[[False]*N for _ in range(N)]
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    print(bfs(x1,y1))

