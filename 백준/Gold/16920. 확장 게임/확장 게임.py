import sys
from collections import deque
input = sys.stdin.readline

N, M, P = map(int, input().split())
speeds = list(map(int, input().split()))
graph = [list(input().strip()) for _ in range(N)]
owners = [0] * P

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 초기 큐 & 초기 소유 수
queues = [deque() for _ in range(P)]
for x in range(N):
    for y in range(M):
        ch = graph[x][y]
        if ch.isdigit():
            p = int(ch) - 1
            queues[p].append((x, y))
            owners[p] += 1

def play_round() -> bool:
    expanded_any = False
    for p in range(P):
        s = speeds[p]
        if not queues[p]:
            continue

        # Si 레벨: 큐 비면 즉시 중단 (여기가 TLE 방지 포인트)
        for _ in range(s):
            if not queues[p]:
                break
            qsize = len(queues[p])
            for _ in range(qsize):
                x, y = queues[p].popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == '.':
                        graph[nx][ny] = str(p + 1)   # 점령 확정 (경합 차단)
                        owners[p] += 1               # 새 점령만 카운트
                        queues[p].append((nx, ny))
                        expanded_any = True
    return expanded_any

while play_round():
    pass

print(*owners)
