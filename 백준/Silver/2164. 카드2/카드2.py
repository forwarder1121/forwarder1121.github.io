import sys
from collections import deque

input=sys.stdin.readline
N=int(input())
queue=deque(range(1,N+1))

while not len(queue)==1:
    queue.popleft()
    queue.rotate(-1)

print(queue[0])