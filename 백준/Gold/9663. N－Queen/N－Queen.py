import sys
input=sys.stdin.readline

N=int(input())


used_cols=[False]*N
used_diag1=[False]*(2*N-1) # row + col
used_diag2=[False]*(2*N-1) # row - col + (N-1)

def can_place(row,col)->bool:
    if used_cols[col]:
        return False
    elif used_diag1[row+col]:
        return False
    elif used_diag2[row-col+N-1]:
        return False
    else:
        return True


def back_tracking(row):
    # base-condition
    if row==N:
        return 1
    count=0
    for col in range(N):
        # pruning
        if not can_place(row,col):
            continue
        # apply
        used_cols[col]=True
        used_diag1[row+col]=True
        used_diag2[row-col+N-1]=True
        count+=back_tracking(row+1)
        # undo
        used_cols[col]=False
        used_diag1[row+col]=False
        used_diag2[row-col+N-1]=False
    return count

print(back_tracking(0))
