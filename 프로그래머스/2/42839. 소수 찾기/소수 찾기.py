from itertools import permutations

def is_prime(n)->bool:
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def solution(numbers):
    
    digits=list(numbers)
    made_numbers=set()
    
    for r in range(1,len(digits)+1):
        for perm in permutations(digits,r):
            num=int("".join(perm))
            made_numbers.add(num)
            
    count=0
    for num in made_numbers:
        if is_prime(num):
            count+=1
            
    return count



