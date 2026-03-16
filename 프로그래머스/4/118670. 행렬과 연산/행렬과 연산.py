from collections import deque
def solution(board, operations):
    
    N=len(board)
    M=len(board[0])
    
    left=deque()
    middle=deque()
    right=deque()
    
    for row in range(N):
        left.append(board[row][0])
        middle.append(deque(board[row][1:-1]))
        right.append(board[row][-1])
    
    for op in operations:
        if op=="ShiftRow":
            left.rotate(1)
            middle.rotate(1)
            right.rotate(1)
        elif op=="Rotate":
            middle[0].appendleft(left.popleft())
            right.appendleft(middle[0].pop())
            middle[N-1].append(right.pop())
            left.append(middle[N-1].popleft())
    
    answer=[]
    for row in range(N):
        tmp=[]
        tmp.append(left[row])
        tmp.extend(middle[row])
        tmp.append(right[row])
        answer.append(tmp)
    return answer