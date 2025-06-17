import sys
input=sys.stdin.readline

N,K=map(int,input().split())
coins=[int(input()) for _ in range(N)]
total=0
for coin in reversed(coins):
    if K>=coin:
        total+=K//coin
        K%=coin

print(total)