import sys
input=sys.stdin.readline

nA,nB=map(int,input().split())

A=set(list(map(int,input().split())))
B=set(list(map(int,input().split())))

result=sorted(A-B)
if result:
    print(len(result))
    print(*result)
else:
    print(0)