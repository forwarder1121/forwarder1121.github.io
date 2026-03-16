def solution(citations):
    citations.sort(reverse=True)
    print(citations)
    for idx,val in enumerate(citations):
        if val<=idx:
            return idx
    return len(citations)
    