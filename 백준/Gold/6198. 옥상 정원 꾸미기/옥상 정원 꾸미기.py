import sys
input=sys.stdin.readline
N=int(input())
towers=[int(input()) for _ in range(N)]

stack=[]
answer=0
for tower in towers:
    while stack and stack[-1]<=tower:
        stack.pop()
    answer+=len(stack)
    stack.append(tower)
print(answer)