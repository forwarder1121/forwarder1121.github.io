import sys
from collections import deque
input=sys.stdin.readline

N,K=map(int,input().split())
SIZE=100001
queue=deque()
discovered=[False]*SIZE

queue.append((N,0))
discovered[N]=True

answer=None
while queue:
    cur_node,cur_time=queue.popleft()

    if cur_node==K:
        answer=cur_time
        break
    for next_node in [cur_node-1,cur_node+1,2*cur_node]:
        if 0<=next_node<SIZE:
            if not discovered[next_node]:
                queue.append((next_node,cur_time+1))
                discovered[next_node]=True

print(answer)