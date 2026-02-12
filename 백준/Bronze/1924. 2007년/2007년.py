import sys
input=sys.stdin.readline


x,y=map(int,input().split())

month_days=[31,28,31,30,31,30,31,31,30,31,30,31]

total=sum(month_days[:x-1])+y-1

week=["MON","TUE","WED","THU","FRI","SAT","SUN"]

print(week[total%7])