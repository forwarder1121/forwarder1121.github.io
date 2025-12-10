import math
def solution(arr):
    nums=[int(arr[i]) for i in range(0,len(arr),2)]
    ops=[arr[i] for i in range(1,len(arr),2)]
    
    N=len(nums)
    INF=math.inf
    
    # dp_max[i][j] : i~j 최대
    # dp_min[i][j] : i~j 최소
    
    dp_max=[[-INF]*N for _ in range(N)]
    dp_min=[[INF]*N for _ in range(N)]
    
    # base
    for i in range(N):
        dp_max[i][i]=nums[i]
        dp_min[i][i]=nums[i]
    
    # DP
    for length in range(2,N+1):
        for i in range(N-length+1):
            j=i+length-1
            
            for k in range(i,j):
                op=ops[k]
                
                leftMax=dp_max[i][k]
                leftMin=dp_min[i][k]
                rightMax=dp_max[k+1][j]
                rightMin=dp_min[k+1][j]
                
                if op=="+":
                    dp_max[i][j]=max(dp_max[i][j],leftMax+rightMax)
                    dp_min[i][j]=min(dp_min[i][j],leftMin+rightMin)
                else:
                    dp_max[i][j]=max(dp_max[i][j],leftMax-rightMin)
                    dp_min[i][j]=min(dp_min[i][j],leftMin-rightMax)
    
    return dp_max[0][N-1]