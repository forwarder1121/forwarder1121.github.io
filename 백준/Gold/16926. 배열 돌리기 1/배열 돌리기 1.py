import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

layers = min(N, M) // 2

for l in range(layers):
    elems = []

    # 위
    for y in range(l, M-l):
        elems.append(A[l][y])
    # 오른쪽
    for x in range(l+1, N-l-1):
        elems.append(A[x][M-l-1])
    # 아래
    for y in range(M-l-1, l-1, -1):
        elems.append(A[N-l-1][y])
    # 왼쪽
    for x in range(N-l-2, l, -1):
        elems.append(A[x][l])

    r = R % len(elems)
    elems = elems[r:] + elems[:r]

    idx = 0
    for y in range(l, M-l):
        A[l][y] = elems[idx]; idx += 1
    for x in range(l+1, N-l-1):
        A[x][M-l-1] = elems[idx]; idx += 1
    for y in range(M-l-1, l-1, -1):
        A[N-l-1][y] = elems[idx]; idx += 1
    for x in range(N-l-2, l, -1):
        A[x][l] = elems[idx]; idx += 1

for row in A:
    print(*row)
