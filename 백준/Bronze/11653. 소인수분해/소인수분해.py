import sys,math
input=sys.stdin.readline

# INPUT
N=int(input())


d=2
while d<=int(math.sqrt(N))+1:
    while N%d==0:
        N//=d
        print(d)
    d+=1

if N>1:
    print(N)