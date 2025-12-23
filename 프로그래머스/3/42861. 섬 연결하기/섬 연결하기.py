def solution(N, costs):
    edges=[]    
    for a,b,cost in costs:
        edges.append((cost,a,b))
    edges.sort()
    
    parent=[0]*N # 0-based
    for i in range(N):
        parent[i]=i
    
    def find_parent(x):
        if parent[x]!=x:
            parent[x]=find_parent(parent[x])
        return parent[x]
    
    def union_parent(a,b):
        a=find_parent(a)
        b=find_parent(b)
        if a<b:
            parent[b]=a
        else:
            parent[a]=b
    
    answer = 0
    for cost,a,b in edges:
        if find_parent(a)!=find_parent(b):
            union_parent(a,b)
            answer+=cost
        
        
    
    
    return answer