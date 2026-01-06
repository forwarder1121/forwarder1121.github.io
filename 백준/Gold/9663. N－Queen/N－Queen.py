import sys
input=sys.stdin.readline

N=int(input())
used_col=[False]*N
used_diag1=[False]*(2*N-1)
used_diag2=[False]*(2*N-1)

def P(row):
    # base-condition
    if row==N:
        return 1
    answer=0
    for col in range(N):
        if not used_col[col] and not used_diag1[row+col] and not used_diag2[row-col+N-1]:
            # apply
            used_col[col]=True
            used_diag1[row+col]=True
            used_diag2[row-col+N-1]=True
            # bfs
            answer+=P(row+1)
            # undo
            used_col[col]=False
            used_diag1[row+col]=False
            used_diag2[row-col+N-1]=False
    return answer

print(P(0))