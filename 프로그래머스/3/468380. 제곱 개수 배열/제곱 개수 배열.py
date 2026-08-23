def solution(arr, L, R):
    
    K=0
    N=len(arr)

    L-=1
    
    last_idx=0
    # a는 brr[s,e)를 점유한다.
    for a in arr:
        s=last_idx
        e=s+a     
        overlap=max(0,min(R,e)-max(L,s))
                
        K+=overlap*a
        last_idx=e


    C=0
    x=0
    Sx=0
    W=R-L
    last_idx=0
    for a in arr:
        s,e=last_idx,last_idx+a
        overlap=max(0,min(W,e)-max(0,s))
        Sx+=overlap*a
        last_idx=e
        
    total=sum(arr)
    if W==total:
        return [K,1]
    
    # Sx는 brr[x,x+W)의 합을 가지고 있다.
    out_value=arr[0] # brr[x]의 값
    out_end=arr[0]   # brr[x]가 처음으로 깨지는 brr상의 인덱스
    out_idx=0 # brr[x]를 만드는 arr상의 인덱스
    in_value=arr[0] # brr[x+W]의 값
    in_end=arr[0]   # brr[x+W]가 처음으로 깨지는 brr상의 인덱스
    in_idx=0 # brr[x+W]를 만든 arr상의 인덱스
    
    while W>=in_end:
        in_idx+=1
        in_end+=arr[in_idx]
        
    in_value=arr[in_idx]
    
    while x<total-W:
        
        delta=in_value-out_value
        next_x=min(out_end,in_end-W)
        
        step_limit=next_x-x # step_limit번 미만으로 이동 가능하다.
        required_amount=K-Sx
        if delta==0:
            if Sx==K:
                C+=step_limit
        elif required_amount%delta==0:
            step=required_amount//delta # step번 이동하면 K 도달 가능.
            if 0<=step<step_limit:
                C+=1
        
        x=next_x  
        Sx+=delta*step_limit
        
        if x==total-W:
            break
            
        if x==out_end:
            out_idx+=1
            out_value=arr[out_idx]
            out_end+=arr[out_idx]
        if x+W==in_end:
            in_idx+=1
            in_value=arr[in_idx]
            in_end+=arr[in_idx]
            
    if Sx == K:
        C += 1
    print("K : ",K) 
    print("C : ",C)
    answer = [K,C]
    return answer