import sys
input=sys.stdin.readline

N=int(input())
MOD=10007
answer=1
for i in range(1,10):
    answer*=(N+i)

for i in range(1,10):
    answer//=i



print(answer%MOD)