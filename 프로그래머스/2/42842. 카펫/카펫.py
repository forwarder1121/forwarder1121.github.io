def solution(brown, yellow):
    
    for h in range(1,int(yellow**0.5)+1):
        if yellow%h==0:
            H=h+2
            W=yellow/h+2
            if W*H==brown+yellow:
                return (W,H)
    
    
    return -1