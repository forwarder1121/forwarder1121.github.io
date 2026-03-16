import math

def solution(cap, n, deliveries, pickups):
    
    answer = 0
    
    S_i = 0  # suffix 배달 누적
    P_i = 0  # suffix 수거 누적
    
    for i in range(n-1, -1, -1):
        
        S_i += deliveries[i]
        P_i += pickups[i]
        
        if S_i <= 0 and P_i <= 0:
            continue
        
        trip_i = max(
            math.ceil(S_i / cap),
            math.ceil(P_i / cap)
        )
        
        answer += trip_i * (i+1) * 2
        
        S_i -= trip_i * cap
        P_i -= trip_i * cap
        
    return answer