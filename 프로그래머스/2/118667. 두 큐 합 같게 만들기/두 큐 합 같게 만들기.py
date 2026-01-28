import math
def solution(q1, q2):
    nums=q1+q2
    #print("nums: ",nums)
    N=len(nums)
    if not sum(nums)%2==0:
        return -1
    target=sum(nums)//2
    
    
    prefix=[0]*N
    for i in range(N):
        prefix[i]=prefix[i-1]+nums[i]
        
    #print("prefix : ",prefix)
    
    start=0
    end=len(q1)-1
    answer=math.inf
    while start<=end and 0<=start<N and 0<=end<N:
        cur_sum=0
        if start==0:
            cur_sum=prefix[end]
        else:
            cur_sum=prefix[end]-prefix[start-1]
        if cur_sum>target:
            start+=1
        elif cur_sum<target:
            end+=1
        else:
            # UPDATE
            cost=start+end-len(q1)+1
            answer=min(answer,cost)
            start+=1
    
    if answer==math.inf:
        return -1
    return answer