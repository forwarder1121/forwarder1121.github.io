import sys
input=sys.stdin.readline

word=input().strip()
lists=[]

for i in range(len(word)):
    lists.append(word[i:])
lists.sort()
print(*lists)