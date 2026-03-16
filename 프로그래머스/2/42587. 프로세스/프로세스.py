from collections import deque

def solution(priorities, location):
   
    queue=deque()
    for index,priority in enumerate(priorities):
        queue.append((priority,index))
    count=0
    
    while queue:
        priority,index=queue.popleft()
        if any(p>priority for p,i in queue):
            queue.append((priority,index))
        else:
            count+=1
            if index==location:
                return count
        
    return -1