from collections import deque,defaultdict
def solution(n, infection, edges, k):
    
    graph=defaultdict(list) # graph[u]=[(v,t), ... ] u와 v는 t로 연결되어 있다.
    for u,v,t in edges:
        graph[u].append((v,t))
        graph[v].append((u,t))
    
    def get_maximum_number_of_infection(infected_set:set,remain:int)->int:
        # remain번 파이브를 열고 닫아 감염시킬 수 있는 최대의 배양체 개수를 반환한다.
        # infected_set는 현재 감염된 배양체의 ID 집합이다.
        
        # base 
        if remain==0:
            return len(infected_set)
        
        # Open pipe
        results=[]
        for pipe in range(1,4):
            new_fected_set=get_infected_set_using(infected_set,pipe)
            ret=get_maximum_number_of_infection(new_fected_set,remain-1)
            results.append(ret)
        return max(results)
    
    # 지금 상태 공유에 뭔가 에러가 있는듯, infected_set 논리가 매끄럽지 않음.
    
    
    def get_infected_set_using(infected_set:set,pipe_number:int)->set:
        # 현재 감염되어 있는 배양체들의 ID 집합은 infected_set으로 주어진다.
        # pipe_number와 일치하는 종류의 파이프만 사용하여 확장된 감염된 배양체 ID 집합을 반환한다.
        new_infected_set=set(infected_set) # 감염된 배양체의 ID 집합
        queue=deque() # 이웃 감염 처리를 기다리고 있는 배양체 ID 집합
        
        for cell in new_infected_set:
            queue.append(cell)
        
        while queue: # 이웃 감염 처리가 아직 안된 배양체가 있는 동안
            cur_cell=queue.popleft() # cur_cell과 이웃한 배양체를 감염시킨다.
            for next_cell,next_pipe in graph[cur_cell]: # cur_cell은 next_cell과 next_pipe로 연결됨.
                if next_pipe==pipe_number: # next_pipe로 연결되어 있다면 감염시킬 수 있으므로
                    if next_cell not in new_infected_set : # next_cell이 미감염체였다면
                        new_infected_set.add(next_cell)
                        queue.append(next_cell) # 감염시키고, 그 또한 이웃을 감염시키도록 한다.
        
        return new_infected_set
                    
                    
        
    answer = get_maximum_number_of_infection({infection},k)
    return answer
    