import sys
input=sys.stdin.readline

N=int(input())
target_sequence=[int(input()) for _ in range(N)]
results=[]
stack=[]
curr=1

for target in target_sequence:
    while curr<=target:
        results.append("+")
        stack.append(curr)
        curr+=1
    if stack and stack[-1]==target:
        stack.pop()
        results.append("-")
    else:
        print("NO")
        sys.exit()

print(*results)
