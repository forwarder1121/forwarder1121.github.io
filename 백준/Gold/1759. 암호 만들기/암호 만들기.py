import sys
from copy import deepcopy
input=sys.stdin.readline

L,C=map(int,input().split())
candidates=sorted(list(input().split()))

vowels=["a","e","i","o","u"]

def check(string):
    v_num=len([s for s in string if s in vowels])
    c_num=len(string)-v_num
    if v_num>=1 and c_num>=2:
        return True
    return False

def P(n,idx,path):
    
    if idx==C:
        if n==L:
            if check(path):
                answer.append(path)
        return
        
    if n==L:
        if check(path):
            answer.append(path)
        return
    
    P(n+1,idx+1,path+candidates[idx])
    P(n,idx+1,path)
    return

answer=[]
P(0,0,"")
print(*answer)