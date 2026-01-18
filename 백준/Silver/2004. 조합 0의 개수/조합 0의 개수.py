import sys,math
input=sys.stdin.readline

N,M=map(int,input().split())

def count(n,p):
    answer=0
    div=p
    while div<=n:
        answer+=n//div
        div*=p
    return answer

numOf2=count(N,2)-count(N-M,2)-count(M,2)
numOf5=count(N,5)-count(N-M,5)-count(M,5)

print(min(numOf2,numOf5))