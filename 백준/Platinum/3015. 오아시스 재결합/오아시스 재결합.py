import sys
input=sys.stdin.readline

N=int(input())
heights=[int(input()) for _ in range(N)]

stack=[] #(height, count) : 같은 키가 연속 몇 명인지
answer=0
for height in heights:
    count=1

    while stack and stack[-1][0]<height:
        answer+=stack[-1][1]
        stack.pop()
    
    if stack and stack[-1][0]==height:
        same=stack.pop()[1]
        answer+=same
        count+=same
    
    if stack:
        answer+=1

    stack.append((height,count))
        
    


print(answer)