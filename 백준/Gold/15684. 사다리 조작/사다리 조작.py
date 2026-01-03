import sys

# 전역 변수 접근 속도를 높이기 위해 함수 내부로 로직을 넣습니다.
def solve():
    input = sys.stdin.readline
    N, M, H = map(int, input().split())
    
    board = [[False] * (N + 1) for _ in range(H + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        board[a][b] = True

    # 가로선이 놓인 상태를 체크하는 함수
    def is_possible():
        for i in range(1, N + 1):
            pos = i
            for j in range(1, H + 1):
                if board[j][pos]:
                    pos += 1
                elif board[j][pos - 1]:
                    pos -= 1
            if pos != i:
                return False
        return True

    def dfs(count, r, c, limit):
        # [가지치기] 현재 홀수 개인 세로선 사이 구간을 계산
        # 이 로직을 넣으면 탐색량이 획기적으로 줄어듭니다.
        if count == limit:
            return is_possible()

        for i in range(r, H + 1):
            start_c = c if i == r else 1
            for j in range(start_c, N):
                if not board[i][j] and not board[i][j-1] and not board[i][j+1]:
                    board[i][j] = True
                    if dfs(count + 1, i, j + 2, limit):
                        return True
                    board[i][j] = False
        return False

    # [핵심 최적화] 홀수 개 가로선 구간 체크
    # i번과 i+1번 세로선 사이의 가로선 개수가 홀수면, 
    # 결국 마지막엔 최소 1개의 가로선이 더 필요하다는 뜻입니다.
    odd_count = 0
    for j in range(1, N):
        count = 0
        for i in range(1, H + 1):
            if board[i][j]:
                count += 1
        if count % 2 != 0:
            odd_count += 1

    # 필요한 최소 가로선 개수가 3개보다 많으면 바로 종료
    if odd_count > 3:
        print(-1)
        return

    # 0개부터 시작
    for limit in range(odd_count, 4): # odd_count부터 시작하는 것도 팁
        if dfs(0, 1, 1, limit):
            print(limit)
            return
            
    print(-1)

solve()