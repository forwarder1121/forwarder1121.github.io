import sys,math
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

INF = math.inf
dp = [[INF] * (1 << N) for _ in range(N)]

dp[0][1] = 0

for mask in range(1 << N):
    for cur in range(N):
        if dp[cur][mask] == INF:
            continue
        for nxt in range(N):
            if mask & (1 << nxt) or W[cur][nxt] == 0:
                continue
            dp[nxt][mask | (1 << nxt)] = min(
                dp[nxt][mask | (1 << nxt)],
                dp[cur][mask] + W[cur][nxt]
            )

res = INF
for cur in range(N):
    if W[cur][0]:
        res = min(res, dp[cur][(1 << N) - 1] + W[cur][0])

print(res)