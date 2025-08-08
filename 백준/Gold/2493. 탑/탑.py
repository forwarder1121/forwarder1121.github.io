import sys
input=sys.stdin.readline

N=int(input())
towers=list(map(int,input().split()))
stack=[] # (index,height)
result=[]

for i in range(N):
    curr_tower=towers[i]
    while stack and stack[-1][1]<curr_tower:
        stack.pop()
    
    if stack:
        result.append(stack[-1][0]+1)
    else:
        result.append(0)
    
    stack.append((i,towers[i]))

print(*result)