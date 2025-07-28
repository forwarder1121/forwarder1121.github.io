import sys
from itertools import combinations
import math
input=sys.stdin.readline

N,M=map(int,input().split())
city=[list(map(int,input().split())) for _ in range(N)]

houses=[]
chickens=[]

for r in range(N):
    for c in range(N):
        if city[r][c]==1:
            houses.append((r,c))
        elif city[r][c]==2:
            chickens.append((r,c))

def get_city_chicken_distance(selected):
    total=0
    for hx,hy in houses:
        distance=math.inf
        for cx,cy in selected:
            distance=min(distance,abs(hx-cx)+abs(hy-cy))
        total+=distance
    return total

answer=math.inf
for comb in combinations(chickens,M):
    answer=min(answer,get_city_chicken_distance(comb))

print(answer)