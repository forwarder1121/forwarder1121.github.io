import heapq
def solution(scovilles, K):
    
    count=0
    heapq.heapify(scovilles)
   
    while scovilles[0]<K:
        
        if len(scovilles)<2:
            return -1
        count+=1
        low1=heapq.heappop(scovilles)
        low2=heapq.heappop(scovilles)
        new_food=low1+low2*2
        heapq.heappush(scovilles,new_food)
    
    
    return count