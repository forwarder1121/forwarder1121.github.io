n,k=map(int, input().split())
coins=[]
result=0
idx=n-1
for _ in range(n):
    coins.append(int(input()))

while True:
    if k==0: break
    if k>=coins[idx]:
        numOfCoin=k//coins[idx]
        k-=numOfCoin*coins[idx]
        result+=numOfCoin
    idx-=1

print(result)

# 10 4200
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000