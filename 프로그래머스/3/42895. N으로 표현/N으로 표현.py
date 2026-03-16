def solution(N, number):
    
    # INIT
    dp=[set() for _ in range(9)]
    dp[1].add(N)
    
    # DP
    for i in range(1,9):
        dp[i].add(int(str(N)*i))
        for j in range(1,i):
            # +,-,*,/
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a+b)
                    dp[i].add(a-b)
                    dp[i].add(a*b)
                    if b!=0:
                        dp[i].add(a/b)
    
    # RESULT
    for i in range(9):
        for element in dp[i]:
            if element==number:
                return i
    return -1