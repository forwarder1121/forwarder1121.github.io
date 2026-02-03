MOD=10007
def solution(N, tops):
    DP=[0]*(2*N+1) # DP[x] : x 삼각형을 덮는 경우의 수
    DP[0]=1
    if tops[0]:
        DP[1]=3
    else:
        DP[1]=2
    for i in range(2,2*N+1):
        if i%2==0: # 짝수 -> 아랫변
            DP[i]=(DP[i-1]+DP[i-2])%MOD
        else: # 홀수 -> 윗변
            # top이 있으면
            if tops[(i-1)//2]:
                DP[i]=(DP[i-1]*2+DP[i-2])%MOD
            else:
                DP[i]=(DP[i-1]+DP[i-2])%MOD
    
    return DP[2*N]