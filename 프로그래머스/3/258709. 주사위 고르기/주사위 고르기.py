from collections import Counter
def solution(dice):
    
    N=len(dice)
    
    def evaluate(path):
        ''' Return number of wins of A
            path[i]=1 -> A, path[i]=2 -> B '''
        A=[]
        B=[]
        for i in range(N):
            if path[i]:
                A.append(dice[i])
            else:
                B.append(dice[i])
                
        def get_dist(dices):
            dist=Counter({0:1})
            for dice in dices:
                new=Counter()
                for val,cnt in dist.items():
                    for face in dice:
                        new[val+face]+=cnt
                dist=new
            return dist
        
        A_list=get_dist(A)
        B_list=get_dist(B)
        
        wins=0
        for a_sum,a_cnt in A_list.items():
            for b_sum,b_cnt in B_list.items():
                if a_sum>b_sum:
                    wins+=a_cnt*b_cnt
        return wins
                
    
    def P(depth,remain,path):
        ''' Returns (maximum number of wins, best path) within current state '''
        # base
        if depth==N:
            if remain==0:
                return evaluate(path),path[:]
            return -1,[]
        best=-1,[]
        path[depth]=0
        best=max(best,P(depth+1, remain,path))
        
        if remain>0:
            path[depth]=1
            best=max(best,P(depth+1,remain-1,path))
        return best
    
    max_win,best_path = P(0,N//2,[0]*N)
    answer=[]
    for i,v in enumerate(best_path):
        if v==1:
            answer.append(i+1)
    
    return answer