def solution(numbers, target):
    
    # DFS -> depth, state(cur_num)
    def dfs(depth,cur_num):
        count=0
        # base condition
        if depth==len(numbers):
            if cur_num==target:
                return 1
            return 0
        
        # apply
        count+=dfs(depth+1,cur_num+numbers[depth])
        count+=dfs(depth+1,cur_num-numbers[depth])
        return count
   
    return dfs(0,0)