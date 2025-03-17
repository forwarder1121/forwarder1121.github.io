#init
COINS=[500,100,50,10,5,1]
ret=0

#input
give=int(input())
remainder=1000-give

#logic
for coin in COINS:
    cnt=remainder//coin
    ret+=cnt
    remainder%=coin

#print
print(ret)


#time complexity : O(1)