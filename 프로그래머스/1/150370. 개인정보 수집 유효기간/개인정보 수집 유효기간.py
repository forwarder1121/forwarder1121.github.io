def solution(today, terms, privacies):
    
    def to_days(date_str):
        Y,M,D=map(int,date_str.split("."))
        return Y*12*28+M*28+D
    
    term_duration=dict()
    for term in terms:
        name,month=term.split()
        term_duration[name]=int(month)
    
    
    today_date=to_days(today)
    
    answer = []
    for idx,privacy in enumerate(privacies):
        collected_date,term_name=privacy.split()
        expired_date=to_days(collected_date)+term_duration[term_name]*28
        if expired_date<=today_date:
            answer.append(idx+1)
        
    return answer