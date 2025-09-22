import sys
from collections import deque
input=sys.stdin.readline

# init
N,M,P=map(int,input().split())
speeds=list(map(int,input().split()))
graph=[list(input().strip()) for _ in range(N)]
owners=[0]*P
dx=[-1,1,0,0]
dy=[0,0,-1,1]

# multi-source bfs -> queue is required to each player
# init queue
queues=[deque() for _ in range(P)]
for x in range(N):
    for y in range(M):
        if graph[x][y].isdigit():
            pid=int(graph[x][y])-1
            queues[pid].append((x,y))
            owners[pid]+=1

def play_round()->bool:
    any_expended=False
    for pid in range(P):
        speed=speeds[pid]
        for _ in range(speed):
            if not queues[pid]:
                break
            qsize = len(queues[pid])
            for _ in range(qsize):
                cx,cy=queues[pid].popleft()
                for i in range(4):
                    nx=cx+dx[i]
                    ny=cy+dy[i]
                    if 0<=nx<N and 0<=ny<M:
                        if graph[nx][ny]=="." :
                            graph[nx][ny]=str(pid+1)
                            queues[pid].append((nx,ny))
                            owners[pid]+=1
                            any_expended=True
    return any_expended

# simulate
while play_round():
   pass

print(*owners)