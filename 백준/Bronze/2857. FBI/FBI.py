import sys,re
input=sys.stdin.readline

records=[input().strip() for _ in range(5)]
PATTERN=re.compile(r"FBI")

result=[]
for idx,record in enumerate(records):
    if PATTERN.search(record):
        result.append(idx+1)

if result:
    print(*result)
else:
    print("HE GOT AWAY!")