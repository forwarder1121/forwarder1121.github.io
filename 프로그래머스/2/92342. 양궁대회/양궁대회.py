def solution(N, info):
    
    info.reverse()
    
    def evaluate(path):
        ''' Return diff, path upon given path '''
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
        return diff, path
    
    def P(depth, remain, path):
        ''' Returns best_diff, best_path within current state '''
        # base-condition
        if depth==11:
            path[0]=remain
            return evaluate(path)
        best=-1,[-1]
        # no pick
        best=max(best,P(depth+1,remain,path[:]))
        # pick
        if remain>info[depth]:
            new_path=path[:]
            new_path[depth]=info[depth]+1
            best=max(best,P(depth+1,remain-info[depth]-1,new_path))
        return best
        
    best_diff, best_path = P(1,N,[0]*11)
    if best_diff>0:
        return best_path[::-1]
    else:
        return [-1]
    