import sys
input=sys.stdin.readline


def sieve(n):
    is_prime=[True]*(n+1)
    limit=int(n**0.5)+1
    is_prime[0]=is_prime[1]=False
    for i in range(2,limit):
        if is_prime[i]:
            for j in range(i*i,n+1,i):
                is_prime[j]=False

    return [i for i,num in enumerate(is_prime) if is_prime[i]]



N=int(input())
sieve_list=sieve(N)
left=right=result=0
curr_sum=0
while(left<=len(sieve_list)):
    if curr_sum<N: # expand
        if right==len(sieve_list):
            break
        curr_sum+=sieve_list[right]
        right+=1
    elif curr_sum>N: # shrink
        curr_sum-=sieve_list[left]
        left+=1
    else:
        result+=1
        curr_sum-=sieve_list[left]
        left+=1

print(result)