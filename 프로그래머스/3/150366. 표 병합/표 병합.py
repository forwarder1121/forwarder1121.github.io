def solution(commands):
    
    SIZE=50
    N=SIZE*SIZE
    
    # Invariant : Only Root have state
    parent=[i for i in range(N)]
    state=[""]*N
    
    def find(node):
        ''' Finds parent of node '''
        # base-condition
        if node==parent[node]:
            return node
        parent[node]=find(parent[node])
        return parent[node]
    
    def union(a,b):
        ''' Unions a,b node according to problem's condition'''
        ra=find(a)
        rb=find(b)
        if ra==rb:
            return
        if state[ra]=="" and state[rb]!="":
            parent[ra]=rb
        else:
            parent[rb]=ra
    
    def to_index(r,c):
        index=(r-1)*SIZE+(c-1)
        return index
    
    answer = []
    for cmd in commands:
        parts=cmd.split()
        oper=parts[0]
        if oper=="PRINT":
            r,c=parts[1:]
            root=find(to_index(int(r),int(c)))
            result=state[root]
            if result:
                answer.append(result)
            else:
                answer.append("EMPTY")
        elif oper=="MERGE":
            r1,c1,r2,c2=map(int,parts[1:])
            union(to_index(r1,c1),to_index(r2,c2))
        elif oper=="UNMERGE":
            r,c=map(int,parts[1:])
            target_node=to_index(r,c)
            root=find(target_node)
            orginal_value=state[root]
            members=[node for node in range(N) if find(node)==root]
            for member in members:
                parent[member]=member
                state[member]=""
            state[target_node]=orginal_value
        elif oper=="UPDATE":
            if len(parts)==4: 
                ''' TYPE 1 : UPDATE r c value '''
                r,c,value=parts[1:]
                root=find(to_index(int(r),int(c)))
                state[root]=value
            else: 
                ''' TYPE 2 : UPDATE value1 value2 '''
                value1,value2=parts[1:]
                selected_nodes=[]
                for node in range(N):
                    if parent[node]==node and state[node]==value1:
                        selected_nodes.append(node)
                for selected_node in selected_nodes:
                    state[selected_node]=value2
    
    return answer