from collections import defaultdict
def solution(info, _edges):
    
    edges=defaultdict(list)
    for a,b in _edges:
        edges[a].append(b)
    
    def P(sheep,wolf,able2visit):
        ''' Return max(sheep) within the current state '''
        # base-condition
        if len(able2visit)==0:
            return sheep
        
        best=-1
        # stop
        best=sheep
        # visit
        for node in able2visit:
            new_able2visit=able2visit.copy()
            new_able2visit.remove(node)
            for new_node in edges[node]:
                new_able2visit.add(new_node)
            if info[node]==0: # 양
                best=max(best,P(sheep+1,wolf,new_able2visit))
            else: # 늑대
                if wolf+1>=sheep:
                    continue
                    best=max(best,P(0,wolf+1,new_able2visit))
                else:
                    best=max(best,P(sheep,wolf+1,new_able2visit))
        return best
            
    answer = P(0,0,{0})
    return answer