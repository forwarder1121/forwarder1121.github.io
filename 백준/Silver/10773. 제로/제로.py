import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
commands=[int(input().strip()) for _ in range(N)]
stack=deque()
for command in commands:
    if command==0:
        stack.pop()
    else:
        stack.append(command)

print(sum(stack))