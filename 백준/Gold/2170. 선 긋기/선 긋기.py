import sys
input=sys.stdin.readline

N=int(input())
lines=[tuple(map(int,input().split())) for _ in range(N)]
lines.sort()
total=0

start,end=lines[0]
for s,e in lines[1:]:
    if s<=end:
        end=max(end,e)
    else:
        total+=end-start
        start,end=s,e
total+=end-start

print(total)
