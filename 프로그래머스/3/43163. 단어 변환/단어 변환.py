from collections import defaultdict,deque
def solution(begin, target, words):
    
    def one_diff(w1,w2):
        count=0
        for i in range(len(w1)):
            if w1[i]!=w2[i]:
                count+=1
        return count==1
    
    # INIT GRAPH
    N=len(words)
    graph=defaultdict(list)
    for u in range(N):
        for v in range(N):
            if one_diff(words[u],words[v]):
                graph[u].append(v)
         
    # BFS (Multi-Source)
    visited=[False]*N
    distance=[0]*N
    queue=deque()
    for i in range(N):
        if one_diff(begin,words[i]):
            queue.append(i)
            visited[i]=True
            distance[i]=1
    
    while queue:
        cur_node=queue.popleft()
        # base-condition
        if words[cur_node]==target:
            return(distance[cur_node])
        for next_node in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node]=True
                distance[next_node]=distance[cur_node]+1
                queue.append(next_node)
                
    return 0