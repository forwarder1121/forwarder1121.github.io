import sys
input=sys.stdin.readline

string=input().strip()
stack=[]
answer=0
for i in range(len(string)):
    if string[i]=="(":
        stack.append("(")
    else:
        stack.pop()
        if string[i-1]=="(":
            answer+=len(stack)
        else: # ")"
            answer+=1
print(answer)