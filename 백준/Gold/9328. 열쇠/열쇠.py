import sys
from collections import deque,defaultdict
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def solve():
    # input
    H,W=map(int,input().split())
    graph=[['.']*(W+2)]+[['.']+list(input().strip())+['.'] for _ in range(H)]+[['.']*(W+2)]
    visited=[[False]*(W+2) for _ in range(H+2)]
    acquired=set(input().strip())

    blocked=defaultdict(list)
    document=0

    # BFS
    queue=deque()
    queue.append((0,0))
    visited[0][0]=True

    while queue:
        cx,cy=queue.popleft()
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<H+2 and 0<=ny<W+2:
                if not visited[nx][ny]:
                    # wall
                    if graph[nx][ny]=="*":
                        continue
                    # blank
                    if graph[nx][ny]==".":
                        queue.append((nx,ny))
                        visited[nx][ny]=True
                    # door
                    if graph[nx][ny].isupper():
                        if graph[nx][ny].lower() in acquired:
                            queue.append((nx,ny))
                            visited[nx][ny]=True
                        else: 
                            blocked[graph[nx][ny].lower()].append((nx,ny))
                    # key
                    if graph[nx][ny].islower():
                        acquired.add(graph[nx][ny])
                        queue.append((nx,ny))
                        visited[nx][ny]=True
                        for bx,by in blocked[graph[nx][ny]]:
                            queue.append((bx,by))
                    # document
                    if graph[nx][ny]=="$":
                        document+=1
                        queue.append((nx,ny))
                        visited[nx][ny]=True

    print(document)

# Main
T=int(input())
for _ in range(T):
    solve()