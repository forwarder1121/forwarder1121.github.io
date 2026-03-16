import sys
input=sys.stdin.readline

N=int(input())
numbers=[int(input()) for _ in range(N)]
numbers.sort(reverse=True)
print(*numbers)