import sys
input=sys.stdin.readline

N,M=map(int,input().split())

route=[]
used=[False]*(N+1) # 1-based

def back_tracking(depth):
    # base-condition
    if depth==M:
        print(*route)
        return 
    for i in range(1,N+1):
        # pruning
        if used[i]:
            continue
        used[i]=True
        route.append(i)
        back_tracking(depth+1)
        # undo
        route.pop()
        used[i]=False

back_tracking(0)