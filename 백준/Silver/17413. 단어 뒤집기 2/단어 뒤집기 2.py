import sys
input=sys.stdin.readline

string=input().strip()
idx=0
result=""
while idx<len(string):
    if string[idx]=="<":
        bucket=""
        while idx<len(string) and string[idx]!=">":
            bucket+=string[idx]
            idx+=1
        bucket+=">"
        result+=bucket
        idx+=1
    elif string[idx]!=" ":
        bucket=""
        while idx<len(string) and not (string[idx]==" " or string[idx]=="<"):
            bucket+=string[idx]
            idx+=1
        result+=bucket[::-1]
    else:
        result+=" "
        idx+=1
print(result)