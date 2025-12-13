def solution(name):
    
    # INIT
    N=len(name)
    required_updown=[]
    max_index=0
    
    # O(N)
    for index,s in enumerate(name):
        target=ord(s)-ord('A')
        required_updown.append(min(target,26-target))
        if not target==0:
            max_index=max(max_index,index)
    
    count_updown=sum(required_updown)
    
    count_leftright=max_index*2
    
    # O(N^2)
    for i in range(N-1):
        next_i=i+1
        while next_i<N and required_updown[next_i]==0:
            next_i+=1
        
        case1=(i*2)+(N-next_i)
        case2=(N-next_i)*2+i
        
        count_leftright=min(count_leftright,case1,case2)
    
    answer=count_updown+count_leftright
    return answer