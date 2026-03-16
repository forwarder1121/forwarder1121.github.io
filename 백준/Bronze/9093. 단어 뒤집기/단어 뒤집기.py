import sys
input=sys.stdin.readline

N=int(input())

for _ in range(N):
    words=input().split()
    answer=[]
    for word in words:
        answer.append("".join(word[::-1]))
    print(" ".join(answer))