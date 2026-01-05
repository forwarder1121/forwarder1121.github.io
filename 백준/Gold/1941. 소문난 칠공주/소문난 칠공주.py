import sys
input = sys.stdin.readline

SIZE = 5
board = [list(input().strip()) for _ in range(SIZE)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

princesses = []
answer = set()

def check(x, y):
    if (x, y) in princesses:
        return False

    Y = 0
    for px, py in princesses:
        if board[px][py] == 'Y':
            Y += 1

    if board[x][y] == 'Y' and Y >= 3:
        return False

    return True

def P():
    if len(princesses) == 7:
        answer.add(frozenset(princesses))  # 🔑 핵심 수정
        return

    for px, py in princesses:
        for d in range(4):
            nx, ny = px + dx[d], py + dy[d]
            if 0 <= nx < SIZE and 0 <= ny < SIZE:
                if check(nx, ny):
                    princesses.append((nx, ny))
                    P()
                    princesses.pop()

for x in range(SIZE):
    for y in range(SIZE):
        princesses.append((x, y))
        P()
        princesses.pop()

print(len(answer))
