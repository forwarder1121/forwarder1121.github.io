import sys
input=sys.stdin.readline

N=int(input())
init_state=list(map(int,input().strip()))
goal_state=list(map(int,input().strip()))

Si=0
for idx,s in enumerate(init_state):
    if s:
        Si+=(1<<idx)

Se=0
for idx,s in enumerate(goal_state):
    if s:
        Se+=(1<<idx)


def simulate(state):
    count=0
    for i in range(N-1):
        if state&(1<<i)!=Se&(1<<i):
            count+=1
            state^=(1<<i)
            if i+1<N:
                state^=(1<<i+1)
            if i+2<N:
                state^=(1<<i+2)
    return count if state==Se else -1

a=simulate(Si)

Si2=Si
Si2^=(1<<0)|(1<<1)
b=simulate(Si2)
if b!=-1:
    b+=1


if a==-1 and b==-1:
    print(-1)
elif a==-1:
    print(b)
elif b==-1:
    print(a)
else:
    print(min(a,b))

