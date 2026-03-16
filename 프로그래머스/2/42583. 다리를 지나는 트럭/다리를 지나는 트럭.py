from collections import deque
def solution(escape_time, limit,truck_weights):
    
    waiting_queue=deque(truck_weights)
    cur_bridge=[] # (truck_weight, age)
    time=1
    
    while True:
        
        time+=1
      
        # loading
       
        loaded_weight=sum([weight for weight, _ in cur_bridge])
       
        if waiting_queue:
            waiting_truck=waiting_queue[0]
            if waiting_truck+loaded_weight<=limit:
                waiting_queue.popleft()
                cur_bridge.append((waiting_truck,0))
       
        
        # forwarding
        for i in range(len(cur_bridge)):
            cur_bridge[i]=(cur_bridge[i][0],cur_bridge[i][1]+1)
        
        # unloading
        new_bridge=[]
    
        for i in range(len(cur_bridge)):
            if cur_bridge[i][1]<escape_time:
                new_bridge.append(cur_bridge[i])
        cur_bridge=new_bridge
        
        
        
        if not cur_bridge and not waiting_queue:
            break
        
        
            
    
    return time