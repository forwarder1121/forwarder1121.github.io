def solution(cap, n, deliveries, pickups):
    
    d_remain=0
    p_remain=0
    
    answer=0
    for i in range(n-1,-1,-1):
        d_remain+=deliveries[i]
        p_remain+=pickups[i]
        
        while d_remain>0 or p_remain>0:
            d_remain-=cap
            p_remain-=cap
            answer+=(i+1)*2
    
    return answer