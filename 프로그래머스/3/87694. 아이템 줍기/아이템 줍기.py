from collections import deque
SIZE=51
SCALE=2
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def solution(rectangles, characterX, characterY, itemX, itemY):
    
    # making graph
    graph=[[False]*SIZE*SCALE for _ in range(SIZE*SCALE)]
    for x1,y1,x2,y2 in rectangles:
        x1,y1,x2,y2=x1*SCALE,y1*SCALE,x2*SCALE,y2*SCALE
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                graph[x][y]=True
    for x1,y1,x2,y2 in rectangles:
        x1,y1,x2,y2=x1*SCALE,y1*SCALE,x2*SCALE,y2*SCALE
        for x in range(x1+1,x2):
            for y in range(y1+1,y2):
                graph[x][y]=False
        
                
    # BFS
    dist=[[-1]*SIZE*SCALE for _ in range(SIZE*SCALE)]
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
            if 0<=nx<SIZE*SCALE and 0<=ny<SIZE*SCALE:
                if graph[nx][ny] and dist[nx][ny]==-1:
                    dist[nx][ny]=dist[cx][cy]+1
                    queue.append((nx,ny))

    return -1