import sys
input=sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]

N,M=map(int,input().split())
cx,cy,cdirect=map(int,input().split())
room=[list(map(int,input().split())) for _ in range(N)]


count=0
def is_near_clear(cx,cy):
    for i in range(4):
        nx=cx+dx[i]
        ny=cy+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if room[nx][ny]==0:
                return False
    return True


while True:
    if room[cx][cy]==0:
        room[cx][cy]=2
        count+=1
    if is_near_clear(cx,cy):
        nx=cx-dx[cdirect]
        ny=cy-dy[cdirect]
        if 0<=nx<N and 0<=ny<M:
            if room[nx][ny]!=1:
                cx,cy=nx,ny
            else:
                break
    else:
        cdirect=(cdirect-1)%4
        nx=cx+dx[cdirect]
        ny=cy+dy[cdirect]
        if room[nx][ny]==0:
            cx,cy=nx,ny
        

print(count)