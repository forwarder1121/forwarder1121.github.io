def solution(arr, L, R):
    
    # 기본 가정 : 구간은 모두 반열린구간이며, 0-based이다.
    L-=1
    
    # 문제 1. K 구하기
    K=0
    e=0
    for a in arr:
        # a는 brr의 구간 [s,e)를 점유한다.
        s,e=e,e+a
        
        overlap=max(0,min(R,e)-max(L,s))
        K+=overlap*a
    
    # 문제 2. C 구하기
    C=0
    W=R-L
    N=len(arr)

    # i는 Slinding-Window의 앞 부분을 생성한 arr 상의 인덱스
    # j는 Slinding-Window의 뒷 부분을 생성한 arr 상의 인덱스
    i,j=0,0
    # ei는 arr[i]가 brr의 인덱스의 마지막 인덱스(미포함)
    # ej는 arr[j]가 brr의 인덱스의 마지막 인덱스(미포함)
    ei,ej=arr[0],None
    e=0
    for k in range(N):
        a=arr[k]
        # a[k]는 brr의 구간 [s,e)를 점유한다.
        s,e=e,e+a
        if s<=W<e:
            j=k
            ej=e
            break
    # i, j, ei, sj 초기화 완료
    
    
    # Sx 초기화
    Sx=0
    e=0
    for a in arr:
        # a는 brr의 구간 [s,e)를 점유한다.
        s,e=e,e+a
        overlap=max(0,min(W,e)-max(0,s))
        Sx+=overlap*a
    
    
    x=0
    total=sum(arr)
    while x+W<total:
        next_x=min(ei,ej-W)
        # brr의 인덱스 구간 [x,next_x)에서는 delta가 일정
        out_value=arr[i]
        in_value=arr[j]
        delta=in_value-out_value
        
        if delta==0:
            if Sx==K:
                C+=next_x-x
        else:
            if (K-Sx)%delta==0:
                t=(K-Sx)//delta
                if 0<=t<next_x-x:
                    C+=1
        
        # x,Sx와 i,j,ei,ej 갱신
        Sx+=(delta)*(next_x-x)
        x=next_x
        if x==ei:
            i+=1
            ei+=arr[i]
        if x==ej-W:
            j+=1
            if j==N:
                break
            ej+=arr[j]
            
    if Sx==K:
        C+=1
    
    
    
    answer = [K,C]
    return answer