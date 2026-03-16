import sys,math,heapq
input=sys.stdin.readline

# input
M,N=map(int,input().split())
graph=[list(map(int,input().strip())) for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dijkstra():
    dist=[[math.inf]*M for _ in range(N)]
    dist[0][0]=0

    pq=[]
    heapq.heappush(pq,(0,0,0))

    while pq:
        cur_cost,cx,cy=heapq.heappop(pq)
        if cur_cost!=dist[cx][cy]:
            continue
        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<N and 0<=ny<M:
                new_cost=cur_cost+graph[nx][ny]
                if new_cost<dist[nx][ny]:
                    dist[nx][ny]=new_cost
                    heapq.heappush(pq,(new_cost,nx,ny))
    
    return dist[N-1][M-1]

print(dijkstra())