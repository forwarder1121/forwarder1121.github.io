import sys
input=sys.stdin.readline

N=int(input())
numbers=list(map(int,input().split()))

stack=[]
answer=[]
for i in range(N-1,-1,-1):
    curr_num=numbers[i]
    while stack and curr_num>=stack[-1]:
        stack.pop()
    if stack:
        answer.append(stack[-1])
    else:
        answer.append(-1)
    stack.append(curr_num)

print(*reversed(answer))