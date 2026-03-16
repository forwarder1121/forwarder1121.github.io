import sys
from collections import Counter
input=sys.stdin.readline

M=int(input())
numbers=Counter(list(map(int,input().split())))

K=int(input())
targets=list(map(int,input().split()))

print(*[numbers[target] for target in targets])