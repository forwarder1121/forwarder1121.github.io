
def solution(friends, gifts):
    
    records=dict.fromkeys(friends,0)
    level=dict.fromkeys(friends,0)
    
    for friend in friends:
        records[friend]=dict.fromkeys(friends,0)
    
    for gift in gifts:
        A,B=gift.split()
        records[A][B]+=1
        level[A]+=1
        level[B]-=1
    
    next_gift=dict.fromkeys(friends,0)
    for person in friends:
        for friend in friends:
            if person==friend:
                continue
            if records[person][friend]>records[friend][person]:
                next_gift[person]+=1
            elif records[person][friend]==records[friend][person]:
                if level[person]>level[friend]:
                    next_gift[person]+=1
    

    answer = max(next_gift.values())
    return answer