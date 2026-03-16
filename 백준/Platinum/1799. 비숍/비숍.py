import sys
from collections import defaultdict
input=sys.stdin.readline

N=int(input())
board=[list(map(int,input().split())) for _ in range(N)]


black=defaultdict(list)
white=defaultdict(list)

for x in range(N):
    for y in range(N):
        if board[x][y]==1:
            if (x+y)%2==0:
                black[x+y].append((x,y))
            else:
                white[x+y].append((x,y))

def solve(candidates):
    used_diag=[False]*(2*N-1)

    def P(idx):
        # base-condition
        if idx==2*N-1:
            return 0

        answer=0
        answer=P(idx+1)

        for cx,cy in candidates[idx]:
            if not used_diag[cy-cx+N-1]:
                used_diag[cy-cx+N-1]=True
                answer=max(answer,P(idx+1)+1)
                used_diag[cy-cx+N-1]=False
        return answer
    return P(0)

print(solve(black)+solve(white))