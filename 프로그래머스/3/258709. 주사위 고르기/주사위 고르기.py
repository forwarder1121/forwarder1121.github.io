from collections import defaultdict
from itertools import combinations

def solution(dices):
    
    def P(given_dices,idx,total,record):
        # base-condition
        if idx==N//2:
            record[total]+=1
            return
        for face in range(6):
            new_face=dices[given_dices[idx]][face]
            P(given_dices,idx+1,total+new_face,record)
               
    N=len(dices) # 0-based
    answer=[]
    max_win_count=-1
    for dice_A in combinations(range(N),N//2):
        dice_B=[]
        for num in range(N):
            if num in dice_A:
                continue
            dice_B.append(num)
        result_A=defaultdict(int)
        result_B=defaultdict(int)  # dict[sum]=frequency
        P(dice_A,0,0,result_A)
        P(dice_B,0,0,result_B)
        win_cnt=0
        for a in result_A:
            for b in result_B:
                if a>b:
                    win_cnt+=result_A[a]*result_B[b]
        if win_cnt>max_win_count:
            max_win_count=win_cnt
            answer=[num+1 for num in dice_A] # 1-based
            
    return answer