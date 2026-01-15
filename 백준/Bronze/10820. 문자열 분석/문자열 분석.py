import sys
input=sys.stdin.readline

# [lower,upper,digit,space]

for line in sys.stdin:
    line=line.rstrip("\n")
    result=[0]*4
    for s in line:
        if s.islower():
            result[0]+=1
        elif s.isupper():
            result[1]+=1
        elif s.isdigit():
            result[2]+=1
        elif s.isspace():
            result[3]+=1
    print(*result)

