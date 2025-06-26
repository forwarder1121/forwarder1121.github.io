import sys
input=sys.stdin.readline

N,M=map(int,input().split())
numbers=list(map(int,input().split()))

left=right=0
current_sum=0
result=0

while True:
    if current_sum<M:
        if right==N:
            break
        current_sum+=numbers[right]
        right+=1
    else:
        current_sum-=numbers[left]
        left+=1
    
    if current_sum==M:
        result+=1

print(result)