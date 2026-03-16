def solution(n, results):
    win = [[False]*n for _ in range(n)]

    # 1. 주어진 결과 반영
    for a, b in results:
        win[a-1][b-1] = True

    # 2. 플로이드 워셜 (전이 관계)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if win[i][k] and win[k][j]:
                    win[i][j] = True

    # 3. 순위 확정 가능한 선수 세기
    answer = 0
    for i in range(n):
        stronger = 0  # 나보다 강한 선수
        weaker = 0    # 나보다 약한 선수

        for j in range(n):
            if win[j][i]:
                stronger += 1
            if win[i][j]:
                weaker += 1

        if stronger + weaker == n - 1:
            answer += 1

    return answer
