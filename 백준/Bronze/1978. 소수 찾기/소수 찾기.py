import sys,math
input=sys.stdin.readline

# INPUT
SIZE=10001
is_prime=[True]*SIZE
N=int(input())
numbers=list(map(int,input().split()))

# SIEVE
is_prime[0]=False
is_prime[1]=False
for i in range(2,int(math.sqrt(SIZE)+1)):
    if is_prime[i]:
        j=2
        while i*j<SIZE:
            is_prime[i*j]=False
            j+=1

answer=0
for number in numbers:
    if is_prime[number]:
        answer+=1
print(answer)