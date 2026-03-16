import heapq,sys

input=sys.stdin.readline

N,M=map(int,input().split())
cards=list(map(int,input().split()))

heapq.heapify(cards)

for _ in range(M):
    x=heapq.heappop(cards)
    y=heapq.heappop(cards)
    new_card=x+y
    heapq.heappush(cards,new_card)
    heapq.heappush(cards,new_card)

print(sum(cards))