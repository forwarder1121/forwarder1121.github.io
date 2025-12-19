import sys,math
input=sys.stdin.readline

N,K=map(int,input().split())
answer=math.comb(N,K)
print(answer)