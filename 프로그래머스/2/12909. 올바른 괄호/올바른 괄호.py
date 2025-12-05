def solution(string):
   
    
    waiting=0
    for s in string:
        if s=="(":
            waiting+=1
        else:
            waiting-=1
            if waiting<0:
                return False
    if waiting>0:
        return False
   

    return True