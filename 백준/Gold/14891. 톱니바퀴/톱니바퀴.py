import sys
from collections import deque
input=sys.stdin.readline

wheels=[deque(list(map(int,input().strip()))) for _ in range(4)]
K=int(input())
commands=[list(map(int,input().split())) for _ in range(K)]

for num,direction in commands:
    idx=num-1 # 0-based
    # 0 : none, 1:clock-wise, -1: counter clock-wise
    dirs=[0,0,0,0]
    dirs[idx]=direction
   
    # propagation
    # to left
    for i in range(idx,0,-1):
        if wheels[i][6]!=wheels[i-1][2]:
            dirs[i-1]=-dirs[i]
        else:
            break

    # to right
    for i in range(idx,3,1):
        if wheels[i][2]!=wheels[i+1][6]:
            dirs[i+1]=-dirs[i]
        else:
            break
    
    # rotate
    for i in range(4):
        if dirs[i]==1:
            wheels[i].rotate(1)
        elif dirs[i]==-1:
            wheels[i].rotate(-1)
    
    
print(sum(wheels[i][0]<<i for i in range(4)))