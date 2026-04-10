import sys
input=sys.stdin.readline

G=int(input())
P=int(input())

parent=[i for i in range(G+1)]
air_plane=[int(input()) for _ in range(P)]

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(x1,x2):
    p1=find(x1)
    p2=find(x2)
    parent[p1]=p2

count=0
for p in air_plane:
    gate=find(p)
    if gate==0:
        break
    count+=1
    union(gate,gate-1)

answer=count
print(answer)