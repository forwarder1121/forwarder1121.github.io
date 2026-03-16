import sys,math
input=sys.stdin.readline

N=int(input())
queries=list(map(int,input().split()))

is_prime=[True]*(1001) # 1-based
is_prime[1]=False

for i in range(2,int(math.sqrt(1001))+1):
    if is_prime[i]:
        j=2
        while i*j<1001:
            is_prime[i*j]=False
            j+=1

print(len([num for num in queries if is_prime[num]]))