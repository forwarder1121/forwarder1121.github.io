from collections import defaultdict

def solution(tickets):
    
    graph=defaultdict(list)
    for a,b in tickets:
        graph[a].append(b)
    
    for source in graph:
        graph[source].sort()
    
    route=["ICN"]
    def dfs(cur,used):
        # base-condition
        if used==len(tickets):
            return True
        for i,next in enumerate(graph[cur]):
            if next is None:
                continue
            graph[cur][i]=None
            route.append(next)
            if dfs(next,used+1):
                return True
            route.pop()
            graph[cur][i]=next
        return False
    
    dfs("ICN",0)
    return route