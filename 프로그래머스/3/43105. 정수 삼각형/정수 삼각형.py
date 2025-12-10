from collections import defaultdict
def solution(triangle):
    
    # DP 0-based
    N=len(triangle)
    DP=[[0]*(level+1) for level in range(N)]
    DP[0][0]=triangle[0][0]
    
    for level in range(1,len(triangle)):
        for index in range(level+1):
            if index==0:
                DP[level][index]=DP[level-1][index]+triangle[level][index]
            elif index==level:
                DP[level][index]=DP[level-1][index-1]+triangle[level][index]
            else:
                DP[level][index]=max(DP[level-1][index-1],DP[level-1][index])+triangle[level][index]
                    
    return max(DP[N-1])
