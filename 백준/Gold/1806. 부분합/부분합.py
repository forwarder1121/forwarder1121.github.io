import sys,math
input=sys.stdin.readline
N,S=map(int,input().split())

numbers=list(map(int,input().split()))

# two pointers
left=right=0
curr_sum=0
min_length=math.inf

while(left<N):
    # expand
    if curr_sum<S:
        if right==N:
            break
        curr_sum+=numbers[right]
        right+=1

    # shrink
    else:
        min_length=min(min_length,right-left)
        curr_sum-=numbers[left]
        left+=1

print(min_length if min_length!=math.inf else 0)
