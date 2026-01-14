import sys
from collections import defaultdict
input=sys.stdin.readline

N=int(input())
expression=input().strip()

alpha2value=[]
for _ in range(N):
    alpha2value.append(int(input()))

stack=[]
for ex in expression:
    if ex.isalpha():
        stack.append(alpha2value[ord(ex)-ord("A")])
    else:
        b=stack.pop()
        a=stack.pop()
        if ex=="+":
            stack.append(a+b)
        elif ex=="-":
            stack.append(a-b)
        elif ex=="*":
            stack.append(a*b)
        else:
            stack.append(a/b)

print(f"{stack[0]:.2f}")