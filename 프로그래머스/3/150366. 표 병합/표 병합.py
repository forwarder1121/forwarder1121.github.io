SIZE=50
parent=[i for i in range(SIZE*SIZE)]
state=["" for _ in range(SIZE*SIZE)]
def pos2node(r,c):
    node_number=(r-1)*SIZE+(c-1)
    return node_number

def solution(commands):
    answer = []
    for command in commands:
        oper=command.split()[0]
        if oper=="PRINT":
            r,c=map(int,command.split()[1:])
            p_target_node=find_parent(pos2node(r,c))
            result=state[p_target_node]
            if result:
                answer.append(result)
            else:
                answer.append("EMPTY")
        elif oper=="MERGE":
            r1,c1,r2,c2=map(int,command.split()[1:])
            p_node1=find_parent(pos2node(r1,c1))
            p_node2=find_parent(pos2node(r2,c2))
            if state[p_node1] and not state[p_node2]:
                union_parent(p_node1,p_node2)
            elif state[p_node2] and not state[p_node1]:
                union_parent(p_node2,p_node1)
            else:
                union_parent(p_node1,p_node2)
                
            
        elif oper=="UNMERGE":
            r,c=map(int,command.split()[1:])
            target_node=pos2node(r,c)
            p_target_node=find_parent(target_node)
            original_value=state[p_target_node]
            unmerged_nodes=[node for node in range(SIZE*SIZE) if find_parent(node)==p_target_node]
            for unmerged_node in unmerged_nodes:     
                state[unmerged_node]=""
                parent[unmerged_node]=unmerged_node
            state[target_node]=original_value
            
        elif oper=="UPDATE":
            argv=list(command.split()[1:])
            if len(argv)==3:
                ''' TYPE 1 : UPDATE r c value '''
                r,c,value=argv
                r=int(r)
                c=int(c)
                target_node=pos2node(r,c)
                p_target_node=find_parent(target_node)
                state[p_target_node]=value
            else:
                ''' TYPE 2 : UPDATE value1 value2 '''
                value1,value2=argv
                selected_nodes=set()
                for node in range(SIZE*SIZE):
                    if state[find_parent(node)]==value1:
                        selected_nodes.add(parent[node])
                for selected_node in selected_nodes:
                    state[selected_node]=value2
    
    return answer


def find_parent(node):
    ''' Returns number of parent node'''
    # base-condition
    if node==parent[node]:
        return node
    parent[node]=find_parent(parent[node])
    return parent[node]

def union_parent(node1,node2):
    ''' Unions node2 to node1 '''
    a=find_parent(node1)
    b=find_parent(node2)
    parent[b]=a
        
        
