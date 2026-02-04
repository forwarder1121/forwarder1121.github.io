def solution(coin, cards):
    N = len(cards)
    TARGET = N + 1
    START = N // 3

    hand = set(cards[:START])   # 초기 손패(공짜)
    pool = set()                # 이후 공개된 카드들(후보로 쌓기)
    idx = START
    rounds = 0

    def take_pair_in_same(S):
        # S 안에서 TARGET 쌍 하나 제거 가능하면 True
        for x in list(S):
            y = TARGET - x
            if y in S and y != x:
                S.remove(x)
                S.remove(y)
                return True
        return False

    def take_pair_between(A, B):
        # A에서 x, B에서 y=TARGET-x 하나 제거 가능하면 True
        for x in list(A):
            y = TARGET - x
            if y in B:
                A.remove(x)
                B.remove(y)
                return True
        return False

    while True:
        # 라운드 시작: 카드 2장 공개
        if idx >= N:
            break
        pool.add(cards[idx])
        pool.add(cards[idx + 1])
        idx += 2

        # 0코인: hand 내부에서 쌍
        if take_pair_in_same(hand):
            rounds += 1
            continue

        # 1코인: hand + pool
        if coin >= 1 and take_pair_between(hand, pool):
            coin -= 1
            rounds += 1
            continue

        # 2코인: pool 내부에서 쌍
        if coin >= 2 and take_pair_in_same(pool):
            coin -= 2
            rounds += 1
            continue

        # 어떤 방식으로도 못 내면 종료
        break

    return rounds+1
