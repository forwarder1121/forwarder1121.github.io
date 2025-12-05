from math import ceil
def solution(progresses, speeds):
    requires_day=[]
    for p,s in zip(progresses,speeds):
        requires_day.append(ceil((100-p)/s))
    
    queue=[] 
    answer=[]
   
    for element in requires_day:
        if not queue or element<=queue[0]:            
            queue.append(element)
        else:
            answer.append(len(queue))
            queue=[element]
        
    answer.append(len(queue))
    return answer