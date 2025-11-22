SCALE=2
SIZE=50
MAX=SCALE*SIZE+1
from collections import deque
def solution(rectangles, characterX, characterY, itemX, itemY):
    
    # Making Graph
    graph=[[False]*MAX for _ in range(MAX)]
    dist=[[-1]*MAX for _ in range(MAX)]
    for x1,y1,x2,y2 in rectangles:
        sx1,sy1,sx2,sy2 = x1*SCALE,y1*SCALE,x2*SCALE,y2*SCALE
        for x in range(sx1,sx2+1):
            for y in range(sy1,sy2+1):
                graph[x][y]=True
    
    for x1,y1,x2,y2 in rectangles:
        sx1,sy1,sx2,sy2 = x1*SCALE,y1*SCALE,x2*SCALE,y2*SCALE
        for x in range(sx1+1,sx2):
            for y in range(sy1+1,sy2):
                graph[x][y]=False
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    # BFS
    queue=deque()
    queue.append((characterX*SCALE,characterY*SCALE))
    dist[characterX*SCALE][characterY*SCALE]=0
    
    while queue:
        cx,cy=queue.popleft()
        if cx==itemX*SCALE and cy==itemY*SCALE:
            return dist[cx][cy]//2
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<MAX and 0<=ny<MAX:
                if graph[nx][ny] and dist[nx][ny]==-1:
                    dist[nx][ny]=dist[cx][cy]+1
                    queue.append((nx,ny))
    
    return -1