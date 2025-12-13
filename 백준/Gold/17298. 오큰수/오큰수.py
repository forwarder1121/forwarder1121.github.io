import sys
input=sys.stdin.readline

# INPUT
N=int(input())
array=list(map(int,input().split()))

answer=[-1]*N
stack=[]
for i in range(N):
    while stack and array[stack[-1]]<array[i]:
        decided_index=stack.pop()
        answer[decided_index]=array[i]
    stack.append(i)

while stack:
    answer[stack.pop()]=-1

print(*answer)
