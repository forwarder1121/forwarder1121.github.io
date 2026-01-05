import sys
input=sys.stdin.readline

N=int(input())
eggs=[list(map(int,input().split())) for _ in range(N)]


answer=0
def dfs(idx):
    
    global answer
    # base-condition
    if idx==N:        
        broken=len([egg for egg in eggs if egg[0]<=0])
        answer=max(answer,broken)
        return
    
    alive_idx=[]
    for i in range(N):
        if i==idx:
            continue
        if eggs[i][0]>0:            
            alive_idx.append(i)         

    if not alive_idx or eggs[idx][0]<=0:
        dfs(idx+1)
        return


    for aidx in alive_idx:
        # do
        before1=eggs[idx][0]
        before2=eggs[aidx][0]
        eggs[idx][0]-=eggs[aidx][1]
        eggs[aidx][0]-=eggs[idx][1]
        # dfs
        dfs(idx+1)
        # undo
        eggs[idx][0]=before1
        eggs[aidx][0]=before2

    return  
            
dfs(0)
print(answer)