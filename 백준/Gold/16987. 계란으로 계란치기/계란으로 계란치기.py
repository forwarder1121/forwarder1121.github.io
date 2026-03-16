import sys
input=sys.stdin.readline

N=int(input())
eggs=[list(map(int,input().split())) for _ in range(N)]

def dfs(idx):
    # base-condition
    if idx==N:        
        return len([egg for egg in eggs if egg[0]<=0])
    
    alive_idx=[]
    for i in range(N):
        if i==idx:
            continue
        if eggs[i][0]>0:            
            alive_idx.append(i)         

    if not alive_idx or eggs[idx][0]<=0:
        return dfs(idx+1)

    answer=0
    for aidx in alive_idx:
        # do
        before1=eggs[idx][0]
        before2=eggs[aidx][0]
        eggs[idx][0]-=eggs[aidx][1]
        eggs[aidx][0]-=eggs[idx][1]
        # dfs
        answer=max(answer,dfs(idx+1))
        # undo
        eggs[idx][0]=before1
        eggs[aidx][0]=before2

    return answer
            

print(dfs(0))
