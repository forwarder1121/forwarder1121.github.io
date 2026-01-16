import sys,math
input=sys.stdin.readline

MAX=int(1e6)
is_prime=[True]*(MAX+1) # 1-based
is_prime[0]=False
is_prime[1]=False
for i in range(2,int(math.sqrt(MAX))+1):
    if is_prime[i]:
        for j in range(i*i,MAX+1,i):
            is_prime[j]=False
    

while True:
    N=int(input())
    if N==0:
        break
    flag=False
    for a in range(3,N//2+1,2):
        if is_prime[a] and is_prime[N-a]:
            print(f"{N} = {a} + {N-a}")
            flag=True
            break
    if not flag:
        print("Goldbach's conjecture is wrong.")
