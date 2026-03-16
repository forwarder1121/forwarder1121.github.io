def solution(prices):
    
    N=len(prices)
    answer=[0]*N
    stack=[]
    for i in range(N):
        while stack and prices[stack[-1]]>prices[i]:
            top_index=stack.pop()
            answer[top_index]=i-top_index
        stack.append(i)
    while stack:
        top_index=stack.pop()
        answer[top_index]=N-top_index-1
     
    return answer