from collections import Counter
def solution(clothes):
    counter=Counter([kind for name,kind in clothes])
    answer = 1
    for kind, value in counter.items():
        answer*=(value+1)
    answer-=1    
    return answer