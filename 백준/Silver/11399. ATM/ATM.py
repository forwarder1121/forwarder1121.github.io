N=int(input())
P=list(map(int,input().split()))
result=0
P.sort()

for idx in range(N):
    result+=P[idx]*(N-idx)

print(result)

# 5
# 3 1 4 3 2