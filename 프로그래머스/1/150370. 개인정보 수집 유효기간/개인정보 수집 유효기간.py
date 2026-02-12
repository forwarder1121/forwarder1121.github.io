def solution(today, terms, privacies):
    
    term_duration=dict()
    for term in terms:
        name,month=term.split()
        term_duration[name]=int(month)
    
    today_year,today_month,today_day=map(int,today.split("."))
    today_date=today_year*12*28+today_month*28+today_day
    
    answer = []
    for idx,privacy in enumerate(privacies):
        collected_date,term_name=privacy.split()
        collected_year,collected_month,collected_day=map(int,collected_date.split("."))
        expired_date=collected_year*12*28+collected_month*28+collected_day+term_duration[term_name]*28
        if expired_date<=today_date:
            answer.append(idx+1)
        
    return answer