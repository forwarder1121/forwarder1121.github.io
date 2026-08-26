import math
def solution(signals):
    
    N=len(signals)
    limit=20**N
    for t in range(1,limit+1):
        is_all_yellow=True
        for traffic_idx in range(N):
            g=signals[traffic_idx][0]
            y=signals[traffic_idx][1]
            T=sum(signals[traffic_idx])
            k0=(t-g-1)//T
            if not g+1+T*k0<=t<=g+y+T*k0:
                is_all_yellow=False
                break
        if is_all_yellow:
            return t
    
    return -1
        
        
