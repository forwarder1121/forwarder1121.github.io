dx=[-1,1,0,0]
dy=[0,0,-1,1]

def solution(game_board, table):
    
    def dfs(board,x,y,block,visited,target):
        visited[x][y]=True
        block.append((x,y))
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if not visited[nx][ny] and board[nx][ny]==target:
                    dfs(board,nx,ny,block,visited,target)
    
    def normalize(block):
        min_x=min(x for x,y in block)
        min_y=min(y for x,y in block)
        normalized_block=[]
        return sorted([(x-min_x,y-min_y) for x,y in block])
        
    def rotate(block):
        rotated=[(y,-x) for x,y in block]
        return normalize(rotated)
    
    N=len(game_board)
    
    # Making spaces
    spaces=[]
    visited=[[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if game_board[i][j]==0 and not visited[i][j]:
                block=[]
                dfs(game_board,i,j,block,visited,0)
                spaces.append(normalize(block))
    
    # Making pieces
    pieces=[]
    visited=[[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if table[i][j]==1 and not visited[i][j]:
                block=[]
                dfs(table,i,j,block,visited,1)
                pieces.append(normalize(block))

    # matching
    answer=0
    used=[False]*len(pieces)
    for space in spaces:
        for i in range(len(pieces)):
            matched=False
            piece=pieces[i]
            if used[i]:
                continue
                
            for _ in range(4):
                if space==piece:
                    answer+=len(piece)
                    used[i]=True
                    matched=True
                    break
                piece=rotate(piece)
            if matched:
                break
    
    return answer