import sys
input=sys.stdin.readline

result=[]
while True:
    string=input().strip()
    if string=="#":
        break
    num=0
    for s in string:
        if s.lower() in ["a","e","i","o","u"]:
            num+=1
    result.append(num)

print(*result)