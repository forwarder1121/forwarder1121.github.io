from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    
    SCALE=2
    rects=[]
    for x1,y1,x2,y2 in rectangle:
        rects.append((x1*SCALE,y1*SCALE,x2*SCALE,y2*SCALE))
    
    board=[[False]*101 for _ in range(101)]
    for x1,y1,x2,y2 in rects:
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                board[x][y]=True
    
    for x1,y1,x2,y2 in rects:
        for x in range(x1+1,x2):
            for y in range(y1+1,y2):
                board[x][y]=False
    
    dist=[[-1]*101 for _ in range(101)]
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    queue=deque()
    queue.append((characterX*SCALE,characterY*SCALE))
    dist[characterX*SCALE][characterY*SCALE]=0
    while queue:
        cx,cy=queue.popleft()
        if cx==itemX*2 and cy==itemY*2:
            return dist[cx][cy]//SCALE
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<101 and 0<=ny<101:
                if board[nx][ny]==True and dist[nx][ny]==-1:
                    dist[nx][ny]=dist[cx][cy]+1
                    queue.append((nx,ny))
                    
        
    
    answer = 0
    return answer