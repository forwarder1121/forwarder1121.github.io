import sys
input=sys.stdin.readline

N=int(input())
prices=[int(input()) for _ in range(N)]
ret=0
prev_price=prices[-1]
for price in reversed(prices[:-1]):
    if(prev_price<=price):
        ret+=price-prev_price+1
        prev_price-=1 
    else:
        prev_price=price
       

print(ret)
        