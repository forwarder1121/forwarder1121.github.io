from collections import deque
import sys
input=sys.stdin.readline

N,K=map(int,input().split())
belts=deque(list(map(int,input().split())))
robots=deque([0]*(2*N))

UP=0
DOWN=N-1

step=0
zero_cnt=0

while True:
    step+=1
    belts.rotate(1)
    robots.rotate(1)
    
    if robots[DOWN]:
        robots[DOWN]=0
    
    for i in range(DOWN-1,-1,-1):
        if robots[i] and not robots[i+1] and belts[i+1]>0:
            robots[i]=0
            robots[i+1]=1
            belts[i+1]-=1
            if belts[i+1]==0:
                zero_cnt+=1
    
    if robots[DOWN]:
        robots[DOWN]=0
    
    if belts[UP]>0 :
        robots[UP]=1
        belts[UP]-=1
        if belts[UP]==0:
            zero_cnt+=1
    
    if zero_cnt>=K:
        print(step)
        break