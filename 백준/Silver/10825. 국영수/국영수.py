import sys
input=sys.stdin.readline

N=int(input())
records=[]
for _ in range(N):
    name,kor,eng,math=input().split()
    records.append((name,int(kor),int(eng),int(math)))

records.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for record in records:
    print(record[0])
    