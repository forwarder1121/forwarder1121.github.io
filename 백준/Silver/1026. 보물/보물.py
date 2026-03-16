N=int(input())
result=0
A=list(map(int,input().split()))
B=list(map(int,input().split()))

A.sort(reverse=True)
B.sort()

for idx in range(N):
    result+=A[idx]*B[idx]
print(result)