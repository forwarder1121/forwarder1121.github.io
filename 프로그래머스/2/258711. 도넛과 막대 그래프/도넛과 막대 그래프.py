from collections import defaultdict
def solution(edges):
    
    in_degree=defaultdict(int)
    out_degree=defaultdict(int)
    NEW_NODE=-1
    max_node=-1
    nodes=set()
    for a,b in edges:
        out_degree[a]+=1
        in_degree[b]+=1
        nodes.add(a)
        nodes.add(b)
    
    for node in nodes:
        if in_degree[node]==0 and out_degree[node]>=2:
            NEW_NODE=node
            break
    
    stick_graph=0
    for node in nodes:
        if out_degree[node]==0:
            stick_graph+=1
    
    eight_graph=0
    for node in nodes:
        if out_degree[node]==2 and in_degree[node]>=2:
            eight_graph+=1
    
    donut_graph=out_degree[NEW_NODE]-stick_graph-eight_graph
    
    return [NEW_NODE,donut_graph,stick_graph,eight_graph]