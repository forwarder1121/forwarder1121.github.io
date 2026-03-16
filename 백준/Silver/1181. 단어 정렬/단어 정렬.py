import sys
input=sys.stdin.readline

N=int(input())
words={input().strip() for _ in range(N)}

sorted_words=sorted(words,key=lambda x: (len(x),x))

print(*sorted_words)