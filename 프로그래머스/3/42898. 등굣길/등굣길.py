CONSTANT=1000000007

def solution(M, N, puddles):
    
    # init
    dp=[[0]*N for _ in range(M)]
    dp[0][0]=1
    
    # DP
    for x in range(N):
        for y in range(M):
            if x==0 and y==0:
                continue
            elif [y+1,x+1] in puddles:
                dp[y][x]=0
            else:
                if y==0:
                    dp[y][x]=dp[y][x-1]
                elif x==0:
                    dp[y][x]=dp[y-1][x]
                else:
                    dp[y][x]=(dp[y-1][x]+dp[y][x-1])%CONSTANT
    print(dp)
    return dp[M-1][N-1]