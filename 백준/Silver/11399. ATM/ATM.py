# O(NlogN)
import sys,heapq
input=sys.stdin.readline

N=int(input())
costs=list(map(int,input().split()))

costs.sort()

answer=sum([(N-i)*val for i,val in enumerate(costs)])
print(answer)