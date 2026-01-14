import sys
input=sys.stdin.readline

expression=input().strip()
result=[]
stack=[]

priority={"+":1,"-":1,"*":2,"/":2}

for s in expression:
    if s.isalpha():
        result.append(s)
    elif s=="(":
        stack.append(s)
    elif s==")":
        while stack and stack[-1]!="(":
            result.append(stack.pop())
        stack.pop()
    else:
        while stack and stack[-1]!="(" and priority[stack[-1]]>=priority[s]:
            result.append(stack.pop())
        stack.append(s)

while stack:
    result.append(stack.pop())

print("".join(result))