

def solution(N, K, COMMANDS):
    
    prv=[i-1 for i in range(N+2)]
    nxt=[i+1 for i in range(N+2)]
    prv[0]=-1
    nxt[N+1]=-1
    
    cur_node=K+1
    stack=[]
    for COMMAND in COMMANDS:
        parts=COMMAND.split()
        if parts[0]=="U":
            X=int(parts[1])
            for _ in range(X):
                cur_node=prv[cur_node]
        elif parts[0]=="D":
            X=int(parts[1])
            for _ in range(X):
                cur_node=nxt[cur_node]
        elif parts[0]=="C":
            stack.append(cur_node)
            p=prv[cur_node]
            n=nxt[cur_node]
            nxt[p]=n
            prv[n]=p
            if not nxt[n]==-1:
                cur_node=nxt[cur_node]
            else:
                cur_node=prv[cur_node]
        elif parts[0]=="Z":
            new_node=stack.pop()
            p=prv[new_node]
            n=nxt[new_node]
            nxt[p]=new_node
            prv[n]=new_node
    
    
    answer = ''
    stack=set(stack)
    for node in range(N):
        if node+1 in stack:
            answer+="X"
        else:
            answer+="O"
    return answer