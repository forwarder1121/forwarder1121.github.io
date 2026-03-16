import sys
from copy import deepcopy
input=sys.stdin.readline

N=int(input())
BASE=[list(map(int,input().split())) for _ in range(N)]

def P(idx,board):
    # base-condition
    if idx==5:
        return max(map(max,board))

    answer=0
    for i in range(4):
        new_board=deepcopy(board)
        # do = move + merge + move
        move(new_board,i)
        merge(new_board,i)
        move(new_board,i)
        # DFS
        answer=max(answer,P(idx+1,new_board))
        # undo is replaced by deepcopy
    return answer


def move(board,i):
    # up
    if i==0:
        for col in range(N):
            nums=[]
            for row in range(N):
                if board[row][col]!=0:
                    nums.append(board[row][col])
            for row in range(N):
                board[row][col]=0       
            row=0
            for num in nums:
                board[row][col]=num
                row+=1
            
    # down
    elif i==2:
        for col in range(N):
            nums=[]
            for row in range(N):
                if board[row][col]!=0:
                    nums.append(board[row][col])
            for row in range(N):
                board[row][col]=0    
            row=N-1
            for num in reversed(nums):
                board[row][col]=num
                row-=1
    # left
    elif i==1:
        for row in range(N):
            nums=[]
            for col in range(N):
                if board[row][col]!=0:
                    nums.append(board[row][col])
            for col in range(N):
                board[row][col]=0    
            col=0
            for num in nums:
                board[row][col]=num
                col+=1
    # right
    elif i==3:
        for row in range(N):
            nums=[]
            for col in range(N):
                if board[row][col]!=0:
                    nums.append(board[row][col])
            for col in range(N):
                board[row][col]=0 
            col=N-1
            for num in reversed(nums):
                board[row][col]=num
                col-=1
            


def merge(board,i):
    # up
    if i==0:
        for col in range(N):
            row=0
            while row<N-1:
                if board[row][col]!=0 and board[row][col]==board[row+1][col]:
                    board[row][col]+=board[row+1][col]
                    board[row+1][col]=0
                    row+=1
                row+=1
    # down
    elif i==2:
        for col in range(N):
            row=N-1
            while row>0:
                if board[row][col]!=0 and board[row][col]==board[row-1][col]:
                    board[row][col]+=board[row-1][col]
                    board[row-1][col]=0
                    row-=1
                row-=1
    # left
    elif i==1:
        for row in range(N):
            col=0
            while col<N-1:
                if board[row][col]!=0 and board[row][col]==board[row][col+1]:
                    board[row][col]+=board[row][col+1]
                    board[row][col+1]=0
                    col+=1
                col+=1
    # right
    elif i==3:
        for row in range(N):
            col=N-1
            while col>0:
                if board[row][col]!=0 and board[row][col]==board[row][col-1]:
                    board[row][col]+=board[row][col-1]
                    board[row][col-1]=0
                    col-=1
                col-=1


print(P(0,BASE))

