import math
def solution(progresses, speeds):
    
    N=len(progresses)
    required_days=[]
    for progress,speed in zip(progresses, speeds):
        required_days.append(math.ceil((100-progress)/speed))
    
    print("required_days : ",required_days)
    answer = []
    stack=[]
    for i in range(N):
        while stack and stack[0]<required_days[i]:
            answer.append(len(stack))
            stack=[]
        stack.append(required_days[i])
    answer.append(len(stack))
    return answer