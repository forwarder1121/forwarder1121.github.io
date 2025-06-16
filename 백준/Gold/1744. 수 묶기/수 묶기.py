import sys
input=sys.stdin.readline

N=int(input())

total=0
positives=[]
negatives=[]
zeros=0
ones=0

for _ in range(N):
    num=int(input())
    if num>1:
        positives.append(num)
    elif num==1:
        ones+=1
    elif num==0:
        zeros+=1
    else:
        negatives.append(num)

positives.sort(reverse=True)
negatives.sort()

for i in range(0,len(positives)-1,2):
    total+=positives[i]*positives[i+1]
if len(positives)%2==1:
    total+=positives[-1]

for i in range(0,len(negatives)-1,2):
    total+=negatives[i]*negatives[i+1]
if len(negatives)%2==1:
    if zeros>0:
        pass
    else:
        total+=negatives[-1]

total+=ones

print(total)