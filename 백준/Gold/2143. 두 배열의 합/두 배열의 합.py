import sys
from collections import defaultdict
input=sys.stdin.readline

T=int(input())
N=int(input())
A=list(map(int,input().split()))
M=int(input())
B=list(map(int,input().split()))

freq_A=defaultdict(int)


prefix_A=[0]*(N+1)
prefix_B=[0]*(M+1)

for i in range(1,N+1):
    prefix_A[i]=prefix_A[i-1]+A[i-1]

for i in range(1,M+1):
    prefix_B[i]=prefix_B[i-1]+B[i-1]


for end in range(1,N+1):
    for start in range(end):
        interval_sum=prefix_A[end]-prefix_A[start]
        freq_A[interval_sum]+=1

answer=0
for end in range(1,M+1):
    for start in range(end):
        interval_sum=prefix_B[end]-prefix_B[start]
        answer+=freq_A[T-interval_sum]

print(answer)