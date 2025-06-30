import sys
input=sys.stdin.readline

N,S=map(int,input().split())
numbers=list(map(int,input().split()))

left=right=sum=0
min_length=100000001

while left<N:
    if sum<S: #expand
        if right==N: 
            break
        sum+=numbers[right]
        right+=1
    elif sum>=S : #shrink
        cur_length=right-left
        min_length=min(cur_length,min_length)
        sum-=numbers[left]
        left+=1
        
        
    

if min_length==100000001:
    min_length=0

print(min_length)