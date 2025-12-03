from collections import defaultdict

def solution(participant, completion):
    
    counter=defaultdict(int)
    for p in participant:
        counter[p]+=1
    for c in completion:
        counter[c]-=1
    
    for name,cnt in counter.items():
        if cnt>0:
            return name