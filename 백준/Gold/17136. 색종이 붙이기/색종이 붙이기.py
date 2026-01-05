import sys
from copy import deepcopy
input=sys.stdin.readline

SIZE=10
board=[list(map(int,input().split())) for _ in range(SIZE)]
used=[0]*6
vacancies=[]
for x in range(SIZE):
    for y in range(SIZE):
        if board[x][y]==1:
            vacancies.append((x,y))

def find_one(): # return position of "one", return (-1,-1) if it's not existed
    for x in range(SIZE):
        for y in range(SIZE):
            if board[x][y]==1:
                return x,y

    return -1,-1

def check(tx,ty,length):
    if tx + length > SIZE or ty + length > SIZE:
        return False
    for x in range(tx,tx+length):
        for y in range(ty,ty+length):
            if 0<=x<SIZE and 0<=y<SIZE:
                if board[x][y]==0:
                    return False
    return True

def place(tx,ty,length,num):
    for x in range(tx,tx+length):
        for y in range(ty,ty+length):
            if 0<=x<SIZE and 0<=y<SIZE:
                board[x][y]=num


def P(): # return minimum num of required paper to fill board
    tx,ty=find_one()
    # base-condition
    if tx==-1 and ty==-1:
        return 0
    
    count=101
    for length in range(5,0,-1):
        if used[length]>=5:
            continue
        if check(tx,ty,length):
            # apply
            place(tx,ty,length,0)
            used[length]+=1
            # recursion
            count=min(count,P()+1)
            # undo
            place(tx,ty,length,1)
            used[length]-=1
    
    return count

answer=P()
print(-1 if answer==101 else answer)