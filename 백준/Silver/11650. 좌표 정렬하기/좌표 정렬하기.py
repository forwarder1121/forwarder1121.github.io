import sys
input=sys.stdin.readline

N=int(input())
coordinates=[list(map(int,input().split())) for _ in range(N)]
coordinates.sort(key=lambda x:(x[0],x[1]))
for coordinate in coordinates:
    print(*coordinate)