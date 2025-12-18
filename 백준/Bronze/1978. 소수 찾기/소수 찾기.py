import sys,math
input=sys.stdin.readline

# INPUT
SIZE=1001
N=int(input())
numbers=list(map(int,input().split()))

# SIEVE
is_prime=[True]*SIZE
is_prime[0]=False
is_prime[1]=False
for i in range(2,int(math.sqrt(SIZE))+1):
    if is_prime[i]:
        j=2
        while i*j<SIZE:
            is_prime[i*j]=False
            j+=1

answer=len([number for number in numbers if is_prime[number]])
print(answer)