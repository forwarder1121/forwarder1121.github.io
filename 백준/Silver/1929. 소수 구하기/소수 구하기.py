import sys,math
input=sys.stdin.readline

M,N=map(int,input().split())

MAX=int(1e6)
is_prime=[True]*(MAX+1) # 1-based
is_prime[1]=False

for i in range(2,int(math.sqrt(MAX))+1):
    if is_prime[i]:
        for j in range(i*i,MAX+1,i):
            is_prime[j]=False

for i in range(M,N+1):
    if is_prime[i]:
        print(i)