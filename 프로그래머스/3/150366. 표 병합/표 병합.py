

def solution(commands):
    
    SIZE=50
    N=SIZE*SIZE
    parent=[i for i in range(N)]
    state=[""]*N


    def to_index(r,c):
        node_number=(r-1)*SIZE+(c-1)
        return node_number


    def find(node):
        ''' Returns number of parent node'''
        # base-condition
        if node==parent[node]:
            return node
        parent[node]=find(parent[node])
        return parent[node]

    def union(a,b):
        ''' Unions node a,b according to condition of problems '''
        ra=find(a)
        rb=find(b)
        if ra==rb:
            return
        if state[ra]=="" and state[rb]!="":
            parent[ra]=rb
        else:
            parent[rb]=ra
    
    answer = []
    for command in commands:
        parts=command.split()
        oper=parts[0]
        if oper=="PRINT":
            r,c=map(int,parts[1:])
            root=find(to_index(r,c))
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
            original_value=state[root]
            
            # 1) collect members first (NO mutation)
            group = []
            for node in range(N):
                if find(node) == root:
                    group.append(node)

            # 2) reset all
            for node in group:
                parent[node] = node
                state[node] = ""

            # 3) only target keeps the value
            
            for node in range(N):
                if find(node)==root:
                    parent[node]=node
                    state[node]=""
            state[target_node] = original_value
            
        elif oper=="UPDATE":
            if len(parts)==4:
                ''' TYPE 1 : UPDATE r c value '''
                r,c,value=parts[1:]
                target_node=to_index(int(r),int(c))
                root=find(target_node)
                state[root]=value
            else:
                ''' TYPE 2 : UPDATE value1 value2 '''
                value1,value2=parts[1:]
                for node in range(N):
                    if find(node)==node and state[node]==value1:
                        state[node]=value2
    
    return answer

