import sys
input=sys.stdin.readline

N=int(input())
clients=[input().split() for _ in range(N)]

clients.sort(key=lambda x:int(x[0]))
for client in clients:
    print(*client)