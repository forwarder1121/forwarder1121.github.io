def solution(id_list, reports, k):
    
    users=dict()
    for _id in id_list:
        users[_id]={
            "reported_cnt":0,
            "reporting_users":set()
        }
    
    
    for report in reports:
        a,b=report.split()
        if b not in users[a]["reporting_users"]:
            users[a]["reporting_users"].add(b)
            users[b]["reported_cnt"]+=1
    
    
    
    reported_users=set() 
    for u in users:
        if users[u]["reported_cnt"]>=k:
            reported_users.add(u)
    
    
    print("reported_users",reported_users)
    answer = []
    for u in users:
        recevied_mail_cnt=0
        for v in users[u]["reporting_users"]:
            if v in reported_users:
                recevied_mail_cnt+=1
        answer.append(recevied_mail_cnt)
    
    return answer