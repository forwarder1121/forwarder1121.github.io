from collections import deque
SIZE=51 # 1-based
SCALE=2
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def solution(rectangles, characterX, characterY, itemX, itemY):
    
    # Transformation by scaling 2
    rectangle=[[x1*2, y1*2, x2*2, y2*2] for x1,y1,x2,y2 in rectangles]
    characterX=characterX*2
    characterY=characterY*2
    itemX=itemX*2
    itemY=itemY*2
    
    
    # INIT GRAPH 
    graph=[[False]*SIZE*SCALE for _ in range(SIZE*SCALE)]
    
    # PAINTING
    for x1,y1,x2,y2 in rectangle:
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                graph[x][y]=True
    
    # FILLING
    for x1,y1,x2,y2 in rectangle:
        for x in range(x1+1,x2):
            for y in range(y1+1,y2):
                graph[x][y]=False
    
    # BFS
    queue=deque()
    visited=[[False]*SIZE*SCALE for _ in range(SIZE*SCALE)]
    distance=[[-1]*SIZE*SCALE for _ in range(SIZE*SCALE)]
    queue.append((characterX,characterY))
    visited[characterX][characterY]=True
    distance[characterX][characterY]=0
    while queue:
        cx,cy=queue.popleft()
        visited
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<SIZE*SCALE and 0<=ny<SIZE*SCALE:
                if not visited[nx][ny] and graph[nx][ny]:
                    distance[nx][ny]=distance[cx][cy]+1
                    visited[nx][ny]=True
                    queue.append((nx,ny))
                    
        
    
    return distance[itemX][itemY]//2