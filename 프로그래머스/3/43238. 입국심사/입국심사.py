def solution(N, times):
    left=1
    right=max(times)*N
    
    def can(time):
        throughput=0
        for t in times:
            throughput+=time//t
        return throughput>=N
    
    answer=0
    while left<=right:
        mid=(left+right)//2
        if can(mid):
            answer=mid
            right=mid-1            
        else:
            left=mid+1
    
    return answer