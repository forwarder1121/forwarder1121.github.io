import heapq,math
from collections import defaultdict
def solution(N, start, end, roads, traps):
    
    # edges[u] : (v,cost)
    original_edge=defaultdict(list)
    reversed_edge=defaultdict(list)
    trap_idx={node:idx for idx,node in enumerate(traps)}
    T=len(trap_idx)
    for P,Q,S in roads:
        original_edge[P].append((Q,S))
        reversed_edge[Q].append((P,S))
        

    answer = None
    pq=[] # (cost,node,state) pop the most cheapest node
    dist=[[math.inf]*(1<<T) for _ in range(N+1)] # 1-based dist[node][state]
    
    heapq.heappush(pq,(0,start,0))
    dist[start][0]=0
    
    while pq:
        cur_cost,cur_node,state=heapq.heappop(pq)

        # clean up
        if cur_cost>dist[cur_node][state]:
            continue
            
        if cur_node==end:
            answer=dist[cur_node][state]
            break
            
        U_is_active=False
        if cur_node in trap_idx:
            if state&(1<<trap_idx[cur_node]):
                U_is_active=True
        print("cur_node : ",cur_node,"state : ",state,"is determined.")
        
        
        for next_node, next_cost in reversed_edge[cur_node]:
            V_is_active=False
            if next_node in trap_idx:
                if state&(1<<trap_idx[next_node]):
                    V_is_active=True
            is_fliped=U_is_active^V_is_active
            if not is_fliped:
                continue
            new_state=state
            if next_node in trap_idx:
                new_state^=(1<<trap_idx[next_node])
            new_cost=cur_cost+next_cost
            if new_cost<dist[next_node][new_state]:
                dist[next_node][new_state]=new_cost
                heapq.heappush(pq,(new_cost,next_node,new_state))
        
        for next_node, next_cost in original_edge[cur_node]:
            V_is_active=False
            if next_node in trap_idx:
                if state&(1<<trap_idx[next_node]):
                    V_is_active=True
            is_fliped=U_is_active^V_is_active
            if is_fliped:
                continue
            new_state=state
            if next_node in trap_idx:
                new_state^=(1<<trap_idx[next_node])
            new_cost=cur_cost+next_cost
            if new_cost<dist[next_node][new_state]:
                dist[next_node][new_state]=new_cost
                heapq.heappush(pq,(new_cost,next_node,new_state))

    answer=min(dist[end])
    
    return answer