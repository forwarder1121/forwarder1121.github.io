def solution(N, K, cmds):
    
    prev=[idx-1 for idx in range(N)]
    next=[idx+1 for idx in range(N)]
    next[N-1]=-1
    
    removed=[]
    cur=K
    
    for cmd in cmds:
        if cmd[0]=="U":
            x=int(cmd.split()[1])
            for _ in range(x):
                cur=prev[cur]
        elif cmd[0]=="D":
            x=int(cmd.split()[1])
            for _ in range(x):
                cur=next[cur]
        elif cmd[0]=="C":
            removed.append((prev[cur],cur,next[cur]))
            
            if prev[cur]!=-1:
                next[prev[cur]]=next[cur]
            if next[cur]!=-1:
                prev[next[cur]]=prev[cur]
                
            if next[cur]!=-1:
                cur=next[cur]
            else:
                cur=prev[cur]
    
        elif cmd[0]=="Z":
            p,c,n=removed.pop()
            if p!=-1:
                next[p]=c
            if n!=-1:
                prev[n]=c
            
    
    answer = ['O']*N
    for _,c,_ in removed:
        answer[c]="X"
    return "".join(answer)