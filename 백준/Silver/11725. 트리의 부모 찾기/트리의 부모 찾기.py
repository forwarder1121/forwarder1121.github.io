import sys
from collections import defaultdict,deque
input=sys.stdin.readline

N=int(input())
edges=defaultdict(list)

for _ in range(N-1):
    u,v=map(int,input().split())
    edges[u].append(v)
    edges[v].append(u)

parent=[-1]*(N+1) # 1-based
queue=deque()
queue.append(1)

while queue:
    cur=queue.popleft()
    for nxt in edges[cur]:
        if parent[nxt]==-1:
            parent[nxt]=cur
            queue.append(nxt)


answer=[p for i,p in enumerate(parent) if i>=2]
print(*answer)