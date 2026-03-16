from collections import defaultdict
def solution(participant, completion):
    candidates=defaultdict(int)
    for p in participant:
        candidates[p]+=1
    for c in completion:
        candidates[c]-=1
    
    for candidate in candidates:
        if candidates[candidate]==1:
            return candidate
    