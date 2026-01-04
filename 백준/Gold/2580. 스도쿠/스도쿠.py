import sys
from copy import deepcopy
input=sys.stdin.readline

# INPUT
board=[list(map(int,input().split())) for _ in range(9)]

row_check = [[False] * 10 for _ in range(9)]
col_check = [[False] * 10 for _ in range(9)]
box_check = [[False] * 10 for _ in range(9)]

vacancies=[]
for x in range(9):
    for y in range(9):
        if board[x][y]==0:
            vacancies.append((x,y))
        else:
            row_check[x][board[x][y]]=True
            col_check[y][board[x][y]]=True
            box_check[(x//3)*3+(y//3)][board[x][y]]=True

def P(idx):
    # base-condition
    if idx==len(vacancies):
        return True
    
    px,py=vacancies[idx]
    box_idx=(px//3)*3+(py//3)
    for num in range(1,10):
        if not row_check[px][num] and not col_check[py][num] and not box_check[box_idx][num]:
            # apply
            board[px][py]=num
            row_check[px][num]=True
            col_check[py][num]=True
            box_check[box_idx][num]=True
            # dfs
            if P(idx+1):
                return True
            # undo
            board[px][py]=0
            row_check[px][num]=False
            col_check[py][num]=False
            box_check[box_idx][num]=False
            
    return False

P(0)
for row in range(9):
    print(*board[row])