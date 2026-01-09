import sys
input=sys.stdin.readline

N=int(input())

numbers=[int(input()) for _ in range(N)]

stack=[]
ops=[]
cur=1
for num in numbers:
    while num>=cur:
        stack.append(cur)
        cur+=1
        ops.append("+")
    if stack and stack[-1]==num:
        stack.pop()
        ops.append("-")
    else:
        print("NO")
        sys.exit()

print(*ops)