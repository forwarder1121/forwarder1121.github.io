def solution(N, info):
    info.reverse()
    
    def evaluate(path):
        ''' evaluate path and return (diff, path) upon given path '''
        ryan=0
        apache=0
        
        for score in range(11):
            if path[score]==0 and info[score]==0:
                continue
            elif path[score]>info[score]:
                ryan+=score
            else:
                apache+=score
        diff=ryan-apache
        return diff,path
                
    
    def P(depth,remain,path):
        ''' Return (best_diff, best_path) within current state '''
        if depth==11:
            return evaluate([remain]+path)
        best=-1,[]
        best=max(best,P(depth+1,remain,path[:]+[0]))
        if remain>info[depth]:
            best=max(best,P(depth+1,remain-info[depth]-1,path[:]+[info[depth]+1]))
        return best
    
    answer=None
    max_diff,best_path = P(1,N,[])
    if max_diff>0:
        answer=best_path[::-1]
    else:
        answer=[-1]
    return answer