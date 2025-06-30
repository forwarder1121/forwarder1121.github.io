import sys
input=sys.stdin.readline

N,M=map(int,input().split())
numbers=list(map(int,input().split()))

left=right=total=0
result=0

while True:
    if total<M:
        if right==N:
            break
        total+=numbers[right]
        right+=1
    elif total>M:
        total-=numbers[left]
        left+=1
    else:
        result+=1
        total-=numbers[left]
        left+=1


print(result)