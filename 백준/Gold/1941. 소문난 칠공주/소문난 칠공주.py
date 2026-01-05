import sys
from collections import deque
from itertools import combinations
input=sys.stdin.readline

SIZE=5
board=[list(input().strip()) for _ in range(SIZE)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]
princesses=[]

answer=0

def xy2num(x,y):
    return x*SIZE+y
def num2xy(num):
    return num//SIZE,num%SIZE

def ispossible(numbers):
    S=0
    for num in numbers:
        x,y=num2xy(num)
        if board[x][y]=="S":
            S+=1
    if S<4:
        return False
    
    # connected check
    queue=deque()
    queue.append(numbers[0])
    visited=[[False]*SIZE for _ in range(SIZE)]
    while queue:        
        cx,cy=num2xy(queue.popleft())
        visited[cx][cy]=True
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<SIZE and 0<=ny<SIZE:
                if not visited[nx][ny] and xy2num(nx,ny) in numbers:
                    visited[nx][ny]=True
                    queue.append(xy2num(nx,ny))
    
    for x in range(SIZE):
        for y in range(SIZE):
            if xy2num(x,y) in numbers and not visited[x][y]:
                return False
    return True

    

answer=0
for team in combinations(range(25),7):
    if ispossible(team):
        answer+=1

print(answer)