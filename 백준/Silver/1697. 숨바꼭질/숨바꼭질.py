import sys
from collections import deque
input=sys.stdin.readline

N,K=map(int,input().split())

def bfs(start,target):
    visited=[False]*100001
    dist=[0]*100001

    queue=deque()
    queue.append(start)
    visited[start]=True

    while queue:
        curr=queue.popleft()

        if curr==target:
            return dist[curr]

        for next_pos in (curr-1,curr+1,curr*2):
            if 0<=next_pos<=100000:
                if not visited[next_pos]:
                    visited[next_pos]=True
                    dist[next_pos]=dist[curr]+1
                    queue.append(next_pos)


print(bfs(N,K))