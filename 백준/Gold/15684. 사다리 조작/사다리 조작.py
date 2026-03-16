import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())

# board[r][c] : r번째 높이에서 c와 c+1 연결 여부
board = [[False]*N for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    board[a-1][b-1] = True

INF = 4  # 문제 조건상 3 초과는 불가능 처리

def simulate():
    # 모든 세로선 i가 i로 내려오는지 확인
    for i in range(N):
        col = i
        for r in range(H):
            if board[r][col]:
                col += 1
            elif col > 0 and board[r][col-1]:
                col -= 1
        if col != i:
            return False
    return True

def P(cnt, start):
    # 이미 3개 초과면 불가능
    if cnt > 3:
        return INF

    # 현재 상태가 정답이면 더 안 놓아도 됨
    if simulate():
        return cnt

    # 3개까지 써봤는데도 안 되면 불가능
    if cnt == 3:
        return INF

    res = INF

    for idx in range(start, H*(N-1)):
        r = idx // (N-1)
        c = idx % (N-1)

        # 놓을 수 없는 경우
        if board[r][c]:
            continue
        if c > 0 and board[r][c-1]:
            continue
        if c < N-2 and board[r][c+1]:
            continue

        # 선택
        board[r][c] = True
        res = min(res, P(cnt + 1, idx + 1))
        board[r][c] = False

    return res

ans = P(0, 0)
print(ans if ans <= 3 else -1)
