import sys
input=sys.stdin.readline

N=9
board=[list(map(int,input().strip())) for _ in range(N)]


row=[[False]*(N+1) for _ in range(N+1)]
col=[[False]*(N+1) for _ in range(N+1)]
box=[[False]*(N+1) for _ in range(N+1)]

blank=[]
for x in range(N):
    for y in range(N):
        if board[x][y]==0:
            blank.append((x,y))
        else:
            num=board[x][y]
            k=(x//3)*3+y//3
            row[x][num]=True
            col[y][num]=True
            box[k][num]=True

def print_answer():
    for row in board:
        print("".join(map(str,row)))

def P(depth):
    # base
    if depth==len(blank):
        print_answer()
        return True
    x,y=blank[depth]
    k=(x//3)*3+y//3
    able2put=[]
    for num in range(1,10):
        if row[x][num]:
            continue
        if col[y][num]:
            continue
        if box[k][num]:
            continue
        able2put.append(num)
    for num in able2put:
        board[x][y]=num
        row[x][num]=True
        col[y][num]=True
        box[k][num]=True
        if P(depth+1):
            return True
        box[k][num]=False
        col[y][num]=False
        row[x][num]=False
        board[x][y]=0

P(0)