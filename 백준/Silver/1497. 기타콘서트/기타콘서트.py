import sys,math
from collections import defaultdict

input=sys.stdin.readline

# INPUT
N,M=map(int,input().split())
guitar=[]
for _ in range(N):
    _,songs=input().split()
    guitar.append(list(songs))


SONGS=0
GUITARS=math.inf


def P(index,used): 
    global SONGS,GUITARS
    # base-condition
    if index==N:
        if SONGS<get_song_num(used):
            SONGS=get_song_num(used)
            GUITARS=get_gitar_num(used)
        elif SONGS==get_song_num(used):
            GUITARS=min(GUITARS,get_gitar_num(used))
        return
    used|=(1<<index)
    P(index+1,used)
    used&=~(1<<index)
    P(index+1,used)

def get_song_num(used):
    able2song=[False]*M
    for gitar_idx in range(N):
        if used&(1<<gitar_idx):
            # gitar_idx는 사용됨.
            # songs[gitar_idx]를 연주할 수 있음
            for song_idx in range(M):
                if guitar[gitar_idx][song_idx]=="Y":
                    able2song[song_idx]=True

    return len([song for song in able2song if song==True])

def get_gitar_num(used): # O(N)
    num=0
    for idx in range(N):
        if used&(1<<idx):
            num+=1
    return num

P(0,0) # O(2^N * NM)
if SONGS==0:
    print(-1)
else:
    print(GUITARS)