def solution(places):
    SIZE=5
    
    
    def check(place):
        board=[]
        for p in place:
            board.append(list(p))
        interviewers=[]
        for x in range(SIZE):
            for y in range(SIZE):
                if board[x][y]=="P":
                    interviewers.append((x,y))
        # interviewers is already sorted
        for i in range(len(interviewers)):
            for j in range(i+1,len(interviewers)):
                sx,sy=interviewers[i]
                ex,ey=interviewers[j]
                dist=abs(sx-ex)+abs(sy-ey)
                if dist==1:
                    return False
                elif dist==2:
                    if sx==ex:
                        if board[sx][sy+1]=="O":
                            return False
                    elif sy==ey:
                        if board[sx+1][sy]=="O":
                            return False
                    elif sy<ey:
                        if board[sx][sy+1]=="O" or board[sx+1][sy]=="O":
                            return False
                    else:
                        if board[sx][sy-1]=="O" or board[sx+1][sy]=="O":
                            return False
        return True
                            
        
                    
    answer = []
    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    
   
    return answer