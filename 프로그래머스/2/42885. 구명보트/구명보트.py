def solution(people, limit):
    N=len(people)
    people.sort() # O(NlogN)
    left=0
    right=N-1
    answer=0
    while left<=right: # O(N)
        total=people[left]+people[right]
        if total<=limit:
            answer+=1
            left+=1
            right-=1
        else:
            answer+=1
            right-=1
    
    # TOTAl time complexity : O(NlogN)
    return answer