import sys
input=sys.stdin.readline

N,M=map(int,input().split())
edges=[tuple(map(int,input().split())) for _ in range(M)]

parent=[node for node in range(N)] # 0-based

def find(node):
    if parent[node]!=node:
        parent[node]=find(parent[node])
    return parent[node]

def union(n1,n2):
    p1=find(n1)
    p2=find(n2)
    if p1<p2:
        parent[p2]=p1
    else:
        parent[p1]=p2

count=1
is_cycle=False
for u,v in edges:
    if find(u)==find(v):
        is_cycle=True
        break
    else:
        union(u,v)
        count+=1

answer=count if is_cycle else 0
print(answer)