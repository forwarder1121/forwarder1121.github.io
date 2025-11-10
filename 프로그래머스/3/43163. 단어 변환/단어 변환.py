import math
def solution(begin, target, words):
    visited=[False]*(len(words))
    def one_diff(a,b)->bool:
        count=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                count+=1
        return count==1
    
    def dfs(state,depth)->int:
        # base-condition
        if state==target:
            return depth
        # apply
        best=math.inf
        for i in range(len(words)):
            if one_diff(words[i],state) and not visited[i]:
                visited[i]=True
                cand=dfs(words[i],depth+1)
                if cand<best:
                    best=cand
                visited[i]=False
        return best
        
    answer=dfs(begin,0)
    
    return 0 if answer==math.inf else answer