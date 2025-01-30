import re

expr = input()
tokens = re.findall(r'\d+|[+\-*/]', expr)

result=int(tokens[0])
stack=[]
stack_mode=False
for idx in range(1,len(tokens)):
    if idx%2==1: # 부호
        if tokens[idx]=='-':
            stack_mode=True
    if idx%2==0: # 숫자
        if stack_mode==False:
            result+=int(tokens[idx])
        if stack_mode==True:
            stack.append(int(tokens[idx]))
for item in stack:
    result-=item
print(result)