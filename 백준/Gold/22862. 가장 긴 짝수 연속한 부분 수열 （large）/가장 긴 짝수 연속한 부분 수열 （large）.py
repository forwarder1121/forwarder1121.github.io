import sys
input=sys.stdin.readline

N,K=map(int,input().split())
numbers=list(map(int,input().split()))

left=right=0
curr_old=0
max_length=0

# [ left , right )

while right<N:
    if curr_old<=K: # expand
        if numbers[right]%2==1:
            curr_old+=1
        right+=1
    else: #shrink
        if numbers[left]%2==1:
            curr_old-=1
        left+=1
    max_length=max(max_length,right-left-curr_old)
    
    #print("left : ",left, " right : ",right, " | curr_old : ",curr_old)


print(max_length)