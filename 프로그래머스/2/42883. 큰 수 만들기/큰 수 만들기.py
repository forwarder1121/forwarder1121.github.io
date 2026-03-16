def solution(number, k):
    stack=[]
    remain=k
    N=len(number)
    for digit in number:
        while stack and stack[-1]<digit and remain>0:
            stack.pop()
            remain-=1
        stack.append(digit)
        
    while stack and remain:
        stack.pop()
        remain-=1
    answer="".join(stack)
    return answer