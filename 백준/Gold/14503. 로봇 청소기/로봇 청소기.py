import sys
input=sys.stdin.readline

N,M=map(int,input().split())
cx,cy,d=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(N)]
visited=[[False]*M for _ in range(N)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]

answer=0
while True:
    if not visited[cx][cy] and maps[cx][cy]==0:
        visited[cx][cy]=True
        answer+=1
    flag=False
    for i in range(4):
        nx=cx+dx[i]
        ny=cy+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if not visited[nx][ny] and maps[nx][ny]==0:
                flag=True
                break
    
    if flag:
        d=(d-1)%4
        nx=cx+dx[d]
        ny=cy+dy[d]
        if 0<=nx<N and 0<=ny<M:
            if not visited[nx][ny] and maps[nx][ny]==0:
                cx,cy=nx,ny
    
    else:
        nx=cx-dx[d]
        ny=cy-dy[d]
        if 0<=nx<N and 0<=ny<M:
            if maps[nx][ny]==0:
                cx,cy=nx,ny
            else:
                break

print(answer)