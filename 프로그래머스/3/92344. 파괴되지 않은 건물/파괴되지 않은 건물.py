def solution(board, skill):
    N=len(board)
    M=len(board[0])
    
    diff=[[0]*(M+1) for _ in range(N+1)]
    
    for t,r1,c1,r2,c2,degree in skill:
        if t==1:
            degree*=-1
        diff[r1][c1]+=degree
        diff[r1][c2+1]-=degree
        diff[r2+1][c1]-=degree
        diff[r2+1][c2+1]+=degree
    
    # horizental
    for x in range(N+1):
        for y in range(1,M+1):
            diff[x][y]+=diff[x][y-1]
            
    # vertical
    for y in range(M+1):
        for x in range(1,N+1):
            diff[x][y]+=diff[x-1][y]
     
    answer = 0
    for x in range(N):
        for y in range(M):
            if board[x][y]+diff[x][y]>=1:
                answer+=1
    return answer