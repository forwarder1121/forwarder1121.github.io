import sys
N=int(input())
towers=list(map(int,input().split()))

stack=[] # (height, 1-based-index)
result=[]
for i in range(N):
    curr_tower=towers[i]

    while stack and stack[-1][0]<curr_tower:
        stack.pop()
    
    if stack:
        result.append(stack[-1][1])
    else:
        result.append(0)
    
    stack.append((curr_tower,i+1))

print(*result)