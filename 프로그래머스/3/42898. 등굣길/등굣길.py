CONSTANT=1000000007

def solution(M, N, puddles):
    
    # init
    dp=[[0]*M for _ in range(N)]
    dp[0][0]=1
    
    # DP
    for i in range(N):
        for j in range(M):
            if i==0 and j==0:
                continue
            elif [j+1,i+1] in puddles:
                dp[i][j]=0
            else:
                if i==0:
                    dp[i][j]=dp[i][j-1]
                elif j==0:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=(dp[i-1][j]+dp[i][j-1])%CONSTANT
    print(dp)
    return dp[N-1][M-1]