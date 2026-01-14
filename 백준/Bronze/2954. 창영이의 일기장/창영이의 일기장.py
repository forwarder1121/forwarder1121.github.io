import sys,re
input=sys.stdin.readline

line=input().strip()

result=re.sub(r"([aeiouAEIOU])p\1",r"\1",line)
print(result)