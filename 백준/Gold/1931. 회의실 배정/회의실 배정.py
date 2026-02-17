import sys
input=sys.stdin.readline

N=int(input())
meetings=[list(map(int,input().split())) for _ in range(N)]

meetings.sort(key=lambda x:(x[1],x[0]))

cur_time=0
answer=0
for start,end in meetings:
    if start>=cur_time:
        cur_time=end
        answer+=1

print(answer)