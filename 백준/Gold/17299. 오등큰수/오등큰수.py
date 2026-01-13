import sys
from collections import Counter
input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
F=Counter(A)

NGF=[-1]*N
stack=[]
for idx in range(N):
    while stack and F[A[stack[-1]]]<F[A[idx]]:
        NGF[stack.pop()]=A[idx]
    stack.append(idx)

print(*NGF)