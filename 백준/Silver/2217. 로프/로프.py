N=int(input())

ropes=[int(input()) for _ in range(N)]
ropes.sort()

max_weight=0
for i in range(N):
    weight=ropes[i]*(N-i)
    max_weight=max(max_weight,weight)

print(max_weight)
