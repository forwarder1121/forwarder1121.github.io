import sys
input=sys.stdin.readline

N,L=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(N)]


def isPossible(road): # O(N)
    used=[False]*N
    for idx in range(1,N):
        if road[idx]==road[idx-1]:
            continue
        if abs(road[idx]-road[idx-1])>1:
            return False
        if road[idx]>road[idx-1]:
            for j in range(idx-L,idx):
                if j<0 or used[j] or road[idx-1]!=road[j]:
                    return False
                used[j]=True
        if road[idx]<road[idx-1]:
            for j in range(idx,idx+L):
                if j>=N or used[j] or road[idx]!=road[j]:
                    return False
                used[j]=True

    return True


# total time - complexity : O(N^2)
answer=0
for row in range(N): # O(N^2)
    if isPossible(board[row]):
        answer+=1
for col in range(N): # O(N^2)
    line=[]
    for row in range(N):
        line.append(board[row][col])
    if isPossible(line):
        answer+=1
print(answer)
