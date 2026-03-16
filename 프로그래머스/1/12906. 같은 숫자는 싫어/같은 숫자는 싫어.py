def solution(arr):
    
    answer = []
    stack=[-1]
    
    
    for element in arr:
        if element!=stack[-1]:
            answer.append(element)
            stack.append(element)
    
    return answer