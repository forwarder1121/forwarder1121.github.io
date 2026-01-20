import re

def solution(dartResult):
    pattern=re.compile(r"(10|[0-9])(S|D|T)(\*|#)?")
    tokens=pattern.findall(dartResult)
    
    scores=[]
    for i, (num, bonus, option) in enumerate(tokens):
        score=int(num)
        
        if bonus=="S":
            score**=1
        elif bonus=="D":
            score**=2
        elif bonus=="T":
            score**=3
            
        if option=="*":
            if i>0:
                scores[i-1]*=2
            score*=2
        elif option=="#":
            score*=-1
            
        scores.append(score)
    
    return sum(scores)