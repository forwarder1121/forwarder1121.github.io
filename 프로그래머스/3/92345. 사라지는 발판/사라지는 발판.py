import math
def solution(board, aloc, bloc):
    
    N=len(board)
    M=len(board[0])    
    
    directions=[(1,0),(-1,0),(0,1),(0,-1)]
    
    def P(ax,ay,bx,by):
        '''
        Return best result within current state
        Returns : (can_win, move_count)
        '''
        # base-condition
        if board[ax][ay]==0:
            return False,0
        can_win=False
        min_moves=math.inf
        max_moves=0
        
        # for choice
        for dx,dy in directions:
            nx,ny=ax+dx,ay+dy
            # if possible edge
            if 0<=nx<N and 0<=ny<M and board[nx][ny]==1:
                board[ax][ay]=0
                oppenent_can_win,moves=P(bx,by,nx,ny)
                board[ax][ay]=1
                
                if not oppenent_can_win:
                    can_win=True
                    min_moves=min(min_moves,moves+1)
                else:
                    max_moves=max(max_moves,moves+1)
        if can_win:
            return True,min_moves
        else:
            return False,max_moves
    
    answer = P(aloc[0],aloc[1],bloc[0],bloc[1])[1]
    return answer