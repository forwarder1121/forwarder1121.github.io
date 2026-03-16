import sys
from collections import defaultdict
input=sys.stdin.readline

N=int(input())

weights=defaultdict(int)
for _ in range(N):
    word=list(input().strip())
    for idx,c in enumerate(word):
        weights[c]+=10**(len(word)-idx-1)

sorted_weights=sorted(weights.values(),reverse=True)

answer=0
digit=9
for w in sorted_weights:
    answer+=w*digit
    digit-=1
print(answer)