import sys,math
input=sys.stdin.readline

# INPUT
N,M=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]

# PREPROCESSING
chickens=[] # (x,y)
houses=[]
for x in range(N):
    for y in range(N):
        if board[x][y]==1:
            houses.append((x,y))
        elif board[x][y]==2:
            chickens.append((x,y))
        
c=len(chickens)

def evaluate(path):
    ''' Returns chicken distance of city upon given path '''
    city_chicken_dist=0
    for hx,hy in houses:
        house_chicken_dist=math.inf
        for i,(cx,cy) in enumerate(chickens):
            if path[i]:
                dist=abs(hx-cx)+abs(hy-cy)
                house_chicken_dist=min(house_chicken_dist,dist)
        city_chicken_dist+=house_chicken_dist
    return city_chicken_dist

def P(depth, remain, path):
    '''Returns best result(min chicken dist) within current state'''
    # base-condition
    if depth==c:
        return evaluate(path)
    best=math.inf
    if remain>0:
        new_path=path[:]
        new_path[depth]=1
        best=min(best,P(depth+1,remain-1,new_path))
    best=min(best,P(depth+1,remain,path[:]))
    return best


answer=P(0,M,[0]*c)
print(answer)