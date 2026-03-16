import sys
input=sys.stdin.readline

N=int(input())
numbers=[int(input()) for _ in range(N)]
numbers.sort()

max_freq=1
current_freq=1
answer=numbers[0]
current_num=numbers[0]

for i in range(1,N):
    if numbers[i]==current_num:
        current_freq+=1
    else:
        if current_freq>max_freq:
            max_freq=current_freq
            answer=current_num
        current_num=numbers[i]
        current_freq=1

if current_freq>max_freq:
    answer=current_num

print(answer)