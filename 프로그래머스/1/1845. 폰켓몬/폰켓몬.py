def solution(nums):
    N=len(nums)
    kinds=set()
    for num in nums:
         kinds.add(num)
    numOfKind=len(kinds)
    
    return min(numOfKind,N//2)