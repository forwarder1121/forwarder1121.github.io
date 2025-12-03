from collections import defaultdict
def solution(nums):
    N=len(nums)
    counter=defaultdict(int)
    for num in nums:
        counter[num]+=1
    
    answer=min(len(counter),N//2)
    
        
    return answer