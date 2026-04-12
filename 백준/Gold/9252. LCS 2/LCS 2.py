# Time Complexity : O(NM)
# N,M is length of each sequence
import sys
input=sys.stdin.readline

A=input().strip()
B=input().strip()

N=len(A)
M=len(B)
dp=[[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        if A[i-1]==B[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

result=""
i=N
j=M
while i>0 and j>0:
    if A[i-1]==B[j-1]:
        result+=A[i-1]
        i-=1
        j-=1
    else:
        if dp[i-1][j]>dp[i][j-1]:
            i-=1
        else:
            j-=1

answer=result[::-1]
print(dp[N][M])
print(answer)