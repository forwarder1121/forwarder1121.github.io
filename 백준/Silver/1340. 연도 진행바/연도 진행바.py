import sys
input=sys.stdin.readline

Month,DD,YYYY,HHMM=input().split()
month=Month
day=int(DD.split(",")[0])
year=int(YYYY)
hour,minute=map(int,HHMM.split(":"))

month_to_idx={"January":0,"February":1,"March":2, "April":3,
"May":4,"June":5,"July":6,"August":7,"September":8,
"October":9,"November":10,"December":11}

days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    if year%400==0:
        return True
    if year%4==0 and year%100!=0:
        return True
    return False

if is_leap(year):
    days[1]=29


total_minute=minute+hour*60+(day-1)*60*24+sum(days[:month_to_idx[month]])*60*24
if is_leap(year):
    print((total_minute/(366*24*60))*100)
else:
    print((total_minute/(365*24*60))*100)