def solution(numbers, target):
    
    def dfs(idx,cur_sum):
        # base-condition
        if idx==len(numbers):
            return 1 if cur_sum==target else 0
        
        plus=dfs(idx+1,cur_sum+numbers[idx])
        minus=dfs(idx+1,cur_sum-numbers[idx])
        
        return plus+minus
        
    
    return dfs(0,0)