def solution(triangle):
    
    # INIT
    N=len(triangle)
    dp=[[0]*level for level in range(1,N+1)] # 0-based
    dp[0][0]=triangle[0][0]
    
    # DP
    for level in range(1,N):
        for index in range(level+1):
            if index==0:
                dp[level][index]=dp[level-1][index]+triangle[level][index]
            elif index==level:
                dp[level][index]=dp[level-1][index-1]+triangle[level][index]
            else:
                dp[level][index]=max(dp[level-1][index-1],dp[level-1][index])+triangle[level][index]                
    
    answer = max(dp[N-1])
    return answer