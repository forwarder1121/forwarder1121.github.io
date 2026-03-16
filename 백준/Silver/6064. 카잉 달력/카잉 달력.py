import sys
import math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())

    # 1. 불가능한 경우 먼저 걸러내기
    g = math.gcd(M, N)
    if (x - y) % g != 0:
        print(-1)
        continue

    # 2. 탐색 범위 (달력이 한 바퀴 도는 시점)
    lcm = M * N // g

    # 3. x가 되는 해들만 확인
    answer = -1
    year = x

    while year <= lcm:
        # 이 해에 y도 맞는지 확인
        if (year - y) % N == 0:
            answer = year
            break
        year += M

    print(answer)
