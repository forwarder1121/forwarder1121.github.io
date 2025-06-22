import sys
from collections import Counter
input=sys.stdin.readline

N=int(input())
numbers=[int(input()) for _ in range(N)]

counter=Counter(numbers)
most_common_freq=counter.most_common()


max_freq = most_common_freq[0][1]

candidates = [num for num, cnt in most_common_freq if cnt == max_freq]
print(min(candidates))