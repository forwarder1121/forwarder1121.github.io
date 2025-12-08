def solution(n, times):
    
    high=max(times)*n
    low=1
    answer=high
    
    def can(T)->bool:
        total=0
        for time in times:
            total+=T//time
            if total>=n:
                return True
        return False
    
    while low<=high:
        mid=(low+high)//2
        if can(mid):
            high=mid-1
            answer=mid
        else:
            low=mid+1
    
    
    
    return answer