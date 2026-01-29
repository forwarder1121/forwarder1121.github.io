
import math
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
    
    DP=[[math.inf]*(max_cop+1) for _ in range(max_alp+1)] # 1-based
    DP[init_alp][init_cop]=0
    for a in range(init_alp,max_alp+1):
        for b in range(init_cop,max_cop+1):
            if DP[a][b]==math.inf:
                continue
            if a+1<=max_alp:
                DP[a+1][b]=min(DP[a+1][b],DP[a][b]+1)
            if b+1<=max_cop:
                DP[a][b+1]=min(DP[a][b+1],DP[a][b]+1)
            for pindex in find_possible_problems(a,b):
                _,_,rwd_a,rwd_c,cost=problems[pindex]
                na=min(max_alp,a+rwd_a)
                nb=min(max_cop,b+rwd_c)
                DP[na][nb]=min(DP[na][nb],DP[a][b]+cost)
    
    
    
    return DP[max_alp][max_cop]
    


