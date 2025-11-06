from collections import deque

def solution(begin, target, words):
    N=len(words)
    visited=[False]*(N+1) # 1-based
    
    def one_diff(a,b)->bool:
        diff=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                diff+=1
        return True if diff==1 else False
    
    queue=deque()
    queue.append((begin,0)) 
    
    while queue:
        cur,depth=queue.popleft()
        if cur==target:
            return depth
        for i in range(N):
            if one_diff(cur,words[i]) and not visited[i]:
                visited[i]=True
                queue.append((words[i],depth+1))
            
    return 0