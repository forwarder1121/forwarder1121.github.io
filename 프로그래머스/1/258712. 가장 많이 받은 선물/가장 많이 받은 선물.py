from collections import defaultdict
def solution(friends, gifts):
    
    records=defaultdict(dict)
    gift_level=dict.fromkeys(friends,0)
    next_gift=dict.fromkeys(friends,0)
    
    for friend in friends:
        records[friend]=dict.fromkeys(friends,0)
    for gift in gifts:
        A,B=gift.split()
        records[A][B]+=1
        gift_level[A]+=1
        gift_level[B]-=1
    
    for person in friends:
        for friend in friends:
            if person==friend:
                continue
            if records[person][friend] or records[friend][person]:
                if records[person][friend]>records[friend][person]: # 많이 줬다면
                    next_gift[person]+=1
            if (records[person][friend]==0 and records[friend][person]==0) or records[person][friend]==records[friend][person]:
                    if gift_level[person]>gift_level[friend]:
                        next_gift[person]+=1
                        
    return max(next_gift.values())