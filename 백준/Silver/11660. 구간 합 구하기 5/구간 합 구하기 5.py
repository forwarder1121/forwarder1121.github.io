import sys
input=sys.stdin.readline

# INPUT
N,M=map(int,input().split())
numbers=[list(map(int,input().split())) for _ in range(N)]

# PREPROCESSING
prefix=[[0]*(N+1) for _ in range(N+1)]
for x in range(1,N+1):
    for y in range(1,N+1):
        prefix[x][y]=prefix[x-1][y]+prefix[x][y-1]-prefix[x-1][y-1]+numbers[x-1][y-1]


# RECTANLGE SUM
answer=[]
for _ in range(M):
    x1,y1,x2,y2=map(int,input().split())
    result=prefix[x2][y2]-prefix[x2][y1-1]-prefix[x1-1][y2]+prefix[x1-1][y1-1]
    answer.append(result)
print(*answer)