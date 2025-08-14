import sys

input=sys.stdin.readline

while True:
    line=list(map(int,input().split()))
    if line[0]==0:
        break
    heights=line[1:]+[0]
    
    # logic
    stack=[] # (start_idx,height)
    answer=0
    for idx, height in enumerate(heights):
        start=idx
        while stack and stack[-1][1]>height:
            start_idx,h=stack.pop()
            area=h*(idx-start_idx)
            answer=max(answer,area)
            start=start_idx
        stack.append((start,height))
    print(answer)
