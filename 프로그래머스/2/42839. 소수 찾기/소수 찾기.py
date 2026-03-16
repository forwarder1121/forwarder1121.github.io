from itertools import permutations

def solution(numbers):
    digits=list(numbers)
    candidates=set()
    for r in range(1,len(numbers)+1):
        for perm in permutations(digits,r):
            candidates.add(int("".join(perm)))
    
    count=0
    for cand in candidates:
        print(type(cand))
        if is_prime(cand):
            count+=1
    return count

def is_prime(num)->bool:
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True