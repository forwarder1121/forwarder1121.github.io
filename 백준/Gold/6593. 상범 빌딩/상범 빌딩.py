import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))
    visited[x][y][z] = 0
    while queue:
        cx, cy, cz = queue.popleft()  # bfs is queue!
        for i in range(6):
            nx = cx + dx[i]
            ny = cy + dy[i]
            nz = cz + dz[i]
            if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C:
                if visited[nx][ny][nz] == -1 and graph[nx][ny][nz] != "#":
                    visited[nx][ny][nz] = visited[cx][cy][cz] + 1
                    if graph[nx][ny][nz] == "E":
                        # 출력 형식 공백 제거
                        print(f"Escaped in {visited[nx][ny][nz]} minute(s).")
                        return
                    queue.append((nx, ny, nz))
    print("Trapped!")

while True:
    # 헤더 줄 앞에 빈 줄이 오면 스킵 (안전용)
    line = input()
    if not line:
        break
    line = line.strip()
    if not line:
        continue

    L, R, C = map(int, line.split())
    if L == 0 and R == 0 and C == 0:
        break

    graph = []
    visited = [[[-1] * C for _ in range(R)] for _ in range(L)]

    # 각 층 읽기: 층 사이의 빈 줄 건너뛰면서 R줄 꽉 채우기
    for _ in range(L):
        floor = []
        while len(floor) < R:
            row = input().strip()
            if row == "":
                continue
            floor.append(list(row))
        graph.append(floor)

    # 시작점 찾아서 BFS 한 번만 실행
    started = False
    for x in range(L):
        if started:
            break
        for y in range(R):
            if started:
                break
            for z in range(C):
                if graph[x][y][z] == "S":
                    bfs(x, y, z)
                    started = True
                    break
