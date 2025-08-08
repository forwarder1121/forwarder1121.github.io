import sys
input=sys.stdin.readline

K=int(input())
requests=[int(input()) for _ in range(K)]
stack=[]
for request in requests:
    if request==0:
        stack.pop()
    else:
        stack.append(request)

print(sum(stack))