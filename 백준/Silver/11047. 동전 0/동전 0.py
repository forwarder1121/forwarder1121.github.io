import sys
input=sys.stdin.readline

N,K=map(int,input().split())
coins=[int(input()) for _ in range(N)]
result=0

for coin in reversed(coins):
    if K>=coin:
        result+=K//coin
        K%=coin
    
print(result)