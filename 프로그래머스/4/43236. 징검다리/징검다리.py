def solution(distance, rocks, n):
    
    # init
    points=[0]+sorted(rocks)+[distance]
  
    def can(mid)->bool:
        count=0
        prev_index=0
        for i in range(1,len(points)):
            if points[i]-points[prev_index]>=mid:
                prev_index=i
            else:
                count+=1
                if count>n:
                    return False
        return True
       
    low=1
    high=distance
    
    answer = 1
    while low<=high:
        mid=(low+high)//2
        if can(mid):
            answer=mid
            low=mid+1
        else:
            high=mid-1
    
    
    return answer