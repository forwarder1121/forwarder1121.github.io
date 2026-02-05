def solution(coin, cards):
    N=len(cards)
    hand=set(cards[:N//3])
    candidates=set()
    ROUND=0
    while True:
        if N//3+ROUND*2==N:
            break
        c1,c2=cards[N//3+ROUND*2],cards[N//3+ROUND*2+1]
        candidates.add(c1)
        candidates.add(c2)
        
        
        # hand 안에 N+1 쌍이 있는 경우
        picked=None
        for card in hand:
            if N+1-card in hand:
                picked=card
                break
        
        if picked:
            hand.remove(picked)
            hand.remove(N+1-picked)
            ROUND+=1
            continue
        
        # 하나는 hand, 하나는 candidates에 있는 경우
        for card in hand:
            if N+1-card in candidates and coin>=1:
                picked=card
                coin-=1
                break
        
        if picked:
            hand.remove(picked)
            candidates.remove(N+1-picked)
            ROUND+=1
            continue
            
        # 두개 다 candidates에 있는 경우
        for card in candidates:
            if N+1-card in candidates and coin>=2:
                picked=card
                coin-=2
                break
        if picked:
            candidates.remove(picked)
            candidates.remove(N+1-picked)
            ROUND+=1
            continue
        # 어떤 경우도 해당하지 않는 경우
        break

        
    return ROUND+1