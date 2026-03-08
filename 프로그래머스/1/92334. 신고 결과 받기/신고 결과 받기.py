from collections import defaultdict
def solution(id_list, reports, k):
    
    edges=defaultdict(set)
    indegree=defaultdict(int)
    for report in reports:
        u,v=report.split()
        if v not in edges[u]:
            edges[u].add(v)
            indegree[v]+=1
    
    black_list=set([node for node in indegree if indegree[node]>=k])
    
    answer=[]
    for node in id_list:
        mail_cnt=0
        for next_node in edges[node]:
            if next_node in black_list:
                mail_cnt+=1
        answer.append(mail_cnt)
    

    return answer