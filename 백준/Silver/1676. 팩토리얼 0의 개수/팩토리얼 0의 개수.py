import sys,math
input=sys.stdin.readline



def factorial(N):
    if N==0:
        return 1
    return N*factorial(N-1)

N=int(input())
result=str(factorial(N))

answer=0
for i in range(len(result)-1,-1,-1):
    if result[i]=="0":
        answer+=1
    else:
        print(answer)
        sys.exit()