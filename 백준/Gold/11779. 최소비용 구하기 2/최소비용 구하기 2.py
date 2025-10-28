import sys,math,heapq
input=sys.stdin.readline

# input
N=int(input())
M=int(input())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
start,end=map(int,input().split())

def dijkstra():
    costs=[math.inf]*(N+1)
    prev=[-1]*(N+1)
    costs[start]=0

    pq=[]
    heapq.heappush(pq,(0,start))
    
    while pq:
        cur_cost,cur_node=heapq.heappop(pq)

        if cur_cost!=costs[cur_node]:
            continue

        for next_cost, next_node in graph[cur_node]:
            new_cost=cur_cost+next_cost
            if new_cost<costs[next_node]:
                costs[next_node]=new_cost
                prev[next_node]=cur_node
                heapq.heappush(pq,(new_cost,next_node))

    path=[]
    cur=end
    while cur!=-1:
        path.append(cur)
        cur=prev[cur]
    path.reverse()

    return costs[end],path

result,path=dijkstra()
print(result)
print(len(path))
print(*path)