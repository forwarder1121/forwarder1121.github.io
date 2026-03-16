from collections import deque
def solution(numbers, target):
    N=len(numbers)
    count=0
    def dfs(state,level):
        count=0
        # base-condition
        if level==N:
            return 1 if state==target else 0
        # do
        count+=dfs(state+numbers[level],level+1)
        count+=dfs(state-numbers[level],level+1)
        # undo
        
        return count
    

    return dfs(0,0)