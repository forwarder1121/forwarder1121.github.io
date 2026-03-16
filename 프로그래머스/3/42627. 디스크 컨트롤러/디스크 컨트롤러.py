import heapq
def solution(jobs):
    
    # INIT
    JOBS=[ (s,i,n) for n,(s,i) in enumerate(jobs)] # (requested_time,number,processing_time)
    JOBS.sort()
    
    print(JOBS)
    
    time=0
    index=0
    ready_pq=[]
    done=0
    total_turnaround=0
    N=len(jobs)
    
    # SIMULATION -> update, do, move
    while done<N:
        
        # update
        while index<N and JOBS[index][0]<=time:
            s,i,n=JOBS[index]
            heapq.heappush(ready_pq,(i,s,n))
            index+=1
            
        # do (index)
        if ready_pq:
            done+=1
            i,s,n=heapq.heappop(ready_pq)
            time+=i
            total_turnaround+=time-s
        # move
        else:
            time=JOBS[index][0]
            
    
    # RESULT
    return total_turnaround//N