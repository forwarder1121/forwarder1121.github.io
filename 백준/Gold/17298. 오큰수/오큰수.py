import sys
input=sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
answer=[-1]*N
stack=[]
for i in range(N):
    curr_num=A[i]
    while stack and A[stack[-1]]<curr_num:
        idx=stack.pop()
        answer[idx]=A[i]
    stack.append(i)
print(*answer)
