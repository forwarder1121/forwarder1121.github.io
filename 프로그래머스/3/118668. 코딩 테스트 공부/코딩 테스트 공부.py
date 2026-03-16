
import math,heapq
def solution(init_alp, init_cop, problems):
    N=len(problems)
    
    max_alp=max(problem[0] for problem in problems)
    max_cop=max(problem[1] for problem in problems)
    
    init_alp = min(init_alp, max_alp)
    init_cop = min(init_cop, max_cop)
    
    
    def find_possible_problems(alp,cop):
        can_be_solved=[]
        for i in range(N): 
            if problems[i][0]<=alp and problems[i][1]<=cop:
                can_be_solved.append(i)
        return can_be_solved
    
    pq=[] # (cost,alp,cop)
    cost=[[math.inf]*(max_cop+1) for _ in range(max_alp+1)] # 1-based
    heapq.heappush(pq,(0,init_alp,init_cop))
    cost[init_alp][init_cop]=0
    
    while pq:
        cur_cost,cur_alp,cur_cop=heapq.heappop(pq)
        
        if cur_alp==max_alp and cur_cop==max_cop:
            return cur_cost
        
        if cur_cost>cost[cur_alp][cur_cop]:
            continue
        
        if cur_alp+1<max_alp+1 and cur_cost+1<cost[cur_alp+1][cur_cop]:
            cost[cur_alp+1][cur_cop]=cur_cost+1
            heapq.heappush(pq,(cur_cost+1,cur_alp+1,cur_cop))
            
        if cur_cop+1<max_cop+1 and cur_cost+1<cost[cur_alp][cur_cop+1]:
            cost[cur_alp][cur_cop+1]=cur_cost+1
            heapq.heappush(pq,(cur_cost+1,cur_alp,cur_cop+1))
        for pidx in find_possible_problems(cur_alp,cur_cop):
            _, _, alp_rwd, cop_rwd, new_cost=problems[pidx]
            
            na=min(cur_alp+alp_rwd,max_alp)
            nb=min(cur_cop+cop_rwd,max_cop)
            
            if cur_cost+new_cost<cost[na][nb]:
                cost[na][nb]=cur_cost+new_cost
                heapq.heappush(pq,(cur_cost+new_cost,na,nb))

    
    
    return -1
    


