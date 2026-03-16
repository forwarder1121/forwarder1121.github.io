import sys
input=sys.stdin.readline

N=int(input())

villages=[]

for _ in range(N):
    x,w=map(int,input().split())
    villages.append((x,w))

villages.sort(key=lambda x:x[0])

total=sum(village[1] for village in villages)
answer=0
cur=0
for i in range(N):
    cur+=villages[i][1]
    if cur>=(total+1)//2:
        answer=villages[i][0]
        break
print(answer)