import sys
input=sys.stdin.readline

N,M=map(int,input().split())
numbers=[int(input()) for _ in range(N)]
numbers.sort()
left=right=0
min_diff=2000000001
while left<N:
    cur_diff=numbers[right]-numbers[left]
    if cur_diff>=M:
        min_diff=min(min_diff,cur_diff)
        left+=1
    else:
        right+=1
        if right==N:
            break
        
        
    
print(min_diff)
