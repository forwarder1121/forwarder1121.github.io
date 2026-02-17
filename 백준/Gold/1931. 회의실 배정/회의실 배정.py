import sys
input=sys.stdin.readline

N=int(input())
meetings=[list(map(int,input().split())) for _ in range(N)]

meetings.sort(key=lambda x:(x[1],x[0]))

cur_time=0
idx=0
answer=0
while True:
    candidates=None
    for i in range(idx,N):
        if meetings[i][0]>=cur_time:
            candidates=meetings[i]
            idx=i+1
            break
    if not candidates:
        break
    
    cur_time=candidates[1]
    answer+=1

print(answer)