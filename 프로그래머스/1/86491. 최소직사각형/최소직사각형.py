import math
def solution(cards):
    
    max_x,max_y=0,0
    for x,y in cards:
        if x<y:
            x,y=y,x
        max_x=max(max_x,x)
        max_y=max(max_y,y)
        
    return max_x*max_y