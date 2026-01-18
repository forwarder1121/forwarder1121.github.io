import sys,math
input=sys.stdin.readline

def f(x,p):
    count=0
    while x%p==0:
        count+=1
        x//=p
    return count

N=int(input())

answer=0
for i in range(1,N+1):
    answer+=f(i,5)
print(answer)