def solution(N, tops):
    MOD=10007
    DP=[0]*(2*N+1)
    DP[0]=1
    if tops[0]:
        DP[1]=3
    else:
        DP[1]=2
    for x in range(2,2*N+1):
        if x%2==1 and tops[x//2]==1:
            DP[x]=(DP[x-1]*2+DP[x-2])%MOD
        else:
            DP[x]=(DP[x-1]+DP[x-2])%MOD
    answer = DP[2*N]
    return answer