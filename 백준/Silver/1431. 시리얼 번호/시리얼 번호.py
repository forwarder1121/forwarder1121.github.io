import sys
input=sys.stdin.readline

N=int(input())
serial_nums=[input().strip() for _ in range(N)]

def extract_sum(word):
    sum=0
    for alpha in word:
        if alpha.isdigit():
            sum+=int(alpha)
    return sum

serial_nums.sort(key=lambda x:(len(x),extract_sum(x),x ))


print(*serial_nums)