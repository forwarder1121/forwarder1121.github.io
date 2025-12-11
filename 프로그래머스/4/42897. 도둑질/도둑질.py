def solution(money):
    
    def rob_linear(arr):
        N=len(arr)
        # init
        dp=[0]*N
        dp[0]=arr[0]
        dp[1]=max(arr[0],arr[1])
        # DP
        for i in range(1,N):
            dp[i]=max(dp[i-2]+arr[i],dp[i-1])
        return dp[N-1]
    
    # CASE 1
    case1=rob_linear(money[:-1])
    # CASE 2
    case2=rob_linear(money[1:])
    
    return max(case1,case2)