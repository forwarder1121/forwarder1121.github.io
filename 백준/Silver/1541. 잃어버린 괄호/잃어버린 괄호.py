import re
#input

input=re.findall(r"\d+|[+-]",input())
result=0
minusAppear=False

for i in range(len(input)):
    # check signal
    if(input[i]=="-"):
        minusAppear=True
        continue
    elif (input[i]=="+"):
        continue
    # logic (number)
    if(minusAppear==False):
        result+=int(input[i])
    else:
        result-=int(input[i])

print(result)

#time complexity : O(N)
#55-50+40