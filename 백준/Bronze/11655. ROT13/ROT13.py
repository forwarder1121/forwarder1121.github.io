import sys
input=sys.stdin.readline

S=input().strip("\n")
result=""
for s in S:
    if s.isupper():
        idx=ord(s)-ord("A")
        idx=(idx+13)%26
        result+=chr(ord("A")+idx)
    elif s.islower():
        idx=ord(s)-ord("a")
        idx=(idx+13)%26
        result+=chr(ord("a")+idx)
    else:
        result+=s
print(result)