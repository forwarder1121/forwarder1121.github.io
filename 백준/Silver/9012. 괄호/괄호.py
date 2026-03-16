import sys
input=sys.stdin.readline

N=int(input())

def check(string):
    stack=[]
    for s in string:
        if s=="(":
            stack.append(s)
        else:
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    else:
        return True


for _ in range(N):
    if check(input().strip()):
        print("YES")
    else:
        print("NO")

