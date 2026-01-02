import sys
from copy import deepcopy
input=sys.stdin.readline

N=int(input())
board=[[0]*N for _ in range(N)]
used=[False]*N
answer=0

diag_1=[False]*(2*N+1) # sum
diag_2=[False]*(2*N+1) # diff

def can_place(row,col):
    if used[col]:
        return False
    if diag_1[row+col]:
        return False
    if diag_2[row-col+N]:
        return False
    return True


def dfs(row):
    # base-condition
    if row==N:
        return 1
    
    result=0
    for col in range(N):
        if can_place(row,col):
            # apply
            diag_1[row+col]=True
            diag_2[row-col+N]=True
            used[col]=True
            # dfs
            result+=dfs(row+1)
            # undo
            diag_1[row+col]=False
            diag_2[row-col+N]=False
            used[col]=False
    
    return result

print(dfs(0))            