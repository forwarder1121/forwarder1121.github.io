from collections import defaultdict
import heapq,math

def solution(N, start, end, roads, traps):
    
    # INPUT
    edges=defaultdict(list)
    reversed_edges=defaultdict(list)
    for p,q,s in roads:
        edges[p].append((q,s))
        reversed_edges[q].append((p,s))
    
    trap_index={}
    for i,node in enumerate(traps):
        trap_index[node]=i
    
    
    # dist[node][state]
    dist=[[math.inf]*(1<<len(traps)) for _ in range(N+1)] # 1-based
    pq=[] # (cost, node, state)
    heapq.heappush(pq,(0,start,0))
    dist[start][0]=0
    while pq:
        cur_cost,cur_node,cur_state=heapq.heappop(pq)
        
        if cur_cost>dist[cur_node][cur_state]:
            continue
            
        if cur_node==end:
            return cur_cost
        # 여기까지 온 (node,state)는 최소 비용으로 확정
        # 연결된 엣지를 탐색
        # 현재 노드와 다음 노드 활성 유무에 따라 사용할 edge의 방향이 달라짐.
        
        # 1. 현재 노드가 활성화 된 상태인가? -> state에서 현재 노드가 활성화되었다고 표기 되었는지 확인
        is_cur_trap_active=False
        if cur_node in traps:
            if cur_state&(1<<trap_index[cur_node]):
                is_cur_trap_active=True
        
        # 2. 다음 노드는 활성화 된 상태인가? -> 다음 노드를 판단하기 위해서 edge 필요
        # 현재 노드가 트랩이였다는 전제하에,
        # 현재 노드 트랩의 활성상태만으로는 엣지 방향을 결정할 수 없음.
        # 결국 정방향 엣지와, 역방향 엣지를 기준으로 다음 노드를 찾고
        # 그 노드의 활성상태를 찾고 -> 이후에 다시 엣지가 유효했는지를 검토해야한다.
        
        # 정방향 엣지
        for next_node,cost in edges[cur_node]:            
            is_next_trap_active=False
            if next_node in traps:
                if cur_state&(1<<trap_index[next_node]):
                    is_next_trap_active=True
            
            # 반전 상태 추적하여 실제로 존재했던 엣지였는지 확인
            is_reversed=is_cur_trap_active^is_next_trap_active
            if is_reversed:
                continue
            
            
            # 유효한 엣지로, 노드 진입[방문]
            # 다음 노드가 트랩이였다면 state update
            new_state=cur_state
            if next_node in traps:
                new_state^=(1<<trap_index[next_node])
            new_cost=cur_cost+cost
            if new_cost<dist[next_node][new_state]:
                dist[next_node][new_state]=new_cost
                heapq.heappush(pq,(new_cost,next_node,new_state))
        
        # 역방향 엣지
        for next_node,cost in reversed_edges[cur_node]:            
            is_next_trap_active=False
            if next_node in traps:
                if cur_state&(1<<trap_index[next_node]):
                    is_next_trap_active=True
            
            # 반전 상태 추적하여 실제로 존재했던 엣지였는지 확인
            is_reversed=is_cur_trap_active^is_next_trap_active
            if not is_reversed:
                continue
            
            
            # 유효한 엣지로, 노드 진입[방문]
            # 다음 노드가 트랩이였다면 state update
            new_state=cur_state
            if next_node in traps:
                new_state^=(1<<trap_index[next_node])
            new_cost=cur_cost+cost
            if new_cost<dist[next_node][new_state]:
                dist[next_node][new_state]=new_cost
                heapq.heappush(pq,(new_cost,next_node,new_state))
    
    return -1