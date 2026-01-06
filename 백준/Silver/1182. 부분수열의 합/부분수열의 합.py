import sys
input=sys.stdin.readline

N,S=map(int,input().split())
arr=list(map(int,input().split()))

def P(state,idx):
    # base-condition
    if idx==N:
        if state==S:
            return 1
        return 0
    
    answer=0
    answer+=P(state+arr[idx],idx+1)
    answer+=P(state,idx+1)

    return answer

answer=P(0,0)
if S==0:
    answer-=1
print(answer)