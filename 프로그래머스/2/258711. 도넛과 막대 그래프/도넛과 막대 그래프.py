from collections import defaultdict
def solution(edges):
    
    NEW_NODE=None
    TOTAL_GRAPH=None
    
    outdegree=defaultdict(int)
    indegree=defaultdict(int)
    nodes=set()
    
    for a,b in edges:
        outdegree[a]+=1
        indegree[b]+=1
        nodes.add(a)
        nodes.add(b)
        
    graph_type = [0,0,0] # [donut, stick, eight]
    for node in nodes:
        if indegree[node]==0 and outdegree[node]>=2:
            NEW_NODE=node
            TOTAL_GRAPH=outdegree[NEW_NODE]
        elif indegree[node]>=2 and outdegree[node]==2:
            graph_type[2]+=1
        elif outdegree[node]==0:
            graph_type[1]+=1
    
    graph_type[0]=TOTAL_GRAPH-graph_type[1]-graph_type[2]
    
    print(graph_type)
    answer=[NEW_NODE,*graph_type]
    return answer