import sys
input=sys.stdin.readline

N=int(input())

for _ in range(N):
    words=input().split()
    answer=""
    for word in words:
        new_word=[]
        for i in range(len(word)-1,-1,-1):
            new_word+=word[i]
        answer+="".join(new_word)
        answer+=" "
    print(answer)