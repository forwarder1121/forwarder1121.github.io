import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    N=int(input())
    prices=list(map(int,input().split()))
    max_price=0
    earnings=0
    for price in reversed(prices):
        if price<max_price: # buy
            earnings+=max_price-price
        else: # sell
            max_price=price
    print(earnings)
