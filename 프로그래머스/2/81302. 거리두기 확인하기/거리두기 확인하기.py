import copy
def solution(places):
    
    N=5
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    def is_safe(place): 
        board=[]
        for x in range(N): # O(N)
            board.append(list(place[x]))
        
        persons=[] # O(N^2)
        for x in range(N):
            for y in range(N):
                if board[x][y]=="P":
                    persons.append((x,y))
        
        
        for px,py in persons: # O(N^2)
            for i in range(4):
                nx=px+dx[i]
                ny=py+dy[i]
                if 0<=nx<N and 0<=ny<N:
                    if board[nx][ny]=="1" or board[nx][ny]=="P":
                        return False
                    if board[nx][ny]=="X":
                        continue
                    board[nx][ny]="1"
        
        return True
    
    
    answer = []
    for place in places:
        if is_safe(place):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer