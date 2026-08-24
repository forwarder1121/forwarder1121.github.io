def solution(cost, hint):
    N=len(cost)
    
    def get_minimum_cost_from(i,having_hints)->int:
        # i stage(0-based)부터 시작하여 끝(N-1) 스테이지까지 해결하여 추가적으로 드는 최소 비용을 반환한다.
        # having_hints는 리스트로, having_hints[k]는 k번째 스테이지의 힌트 개수를 나타낸다.
        # 0 ~ N-1 까지 유효 인덱스
        having_hints=having_hints[:]
        # base-condition
        if i==N-1:
            num_available_hint=min(having_hints[N-1],N-1)
            return cost[N-1][num_available_hint]
        
        # 현재 i stage의 해결비용
        num_available_hint=min(having_hints[i],N-1)
        sol_cost=cost[i][num_available_hint]
        
        # 힌트 구매하지 않는 경우
        no_perphase=sol_cost+get_minimum_cost_from(i+1,having_hints)
        
        # 힌트 구매하는 경우
        # 힌트 구매 비용
        hint_cost=hint[i][0]
        # 구매하는 힌트들
        # hint[i][1],hint[i][2], ... 
        for j in range(1,len(hint[i])):
            stage=hint[i][j]-1
            having_hints[stage]+=1
        
            
        yes_perphase=sol_cost+hint_cost+get_minimum_cost_from(i+1,having_hints)
        
        return min(no_perphase,yes_perphase)

    answer = get_minimum_cost_from(0,[0]*N)
    return answer