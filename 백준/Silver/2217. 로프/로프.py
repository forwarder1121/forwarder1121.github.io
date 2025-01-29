n=int(input())
ropes=[]; result=0
for _ in range(n):
    ropes.append(int(input()))
ropes.sort() # O(nlogn)

for idx in range(n): # O(n)
    result=max(result,ropes[idx]*(n-idx))

# total time complexity : O(nlogn)
print(result)