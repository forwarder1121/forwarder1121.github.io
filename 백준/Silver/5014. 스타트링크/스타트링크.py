import sys
from collections import deque
input=sys.stdin.readline

F,S,G,U,D=map(int,input().split())
visited=[False]*(F+1)
dist=[0]*(F+1)

def bfs(start,target):
    queue=deque()
    queue.append(start)
    visited[start]=True
    while queue:
        curr=queue.popleft()
        if curr==target:
            return dist[curr]
        for next_pos in (curr+U,curr-D):
            if 1<=next_pos<=F:
                if not visited[next_pos]:
                    visited[next_pos]=True
                    dist[next_pos]=dist[curr]+1
                    
                    queue.append(next_pos)
    
    return "use the stairs"


print(bfs(S,G))