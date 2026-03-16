import sys,math
from itertools import combinations
input=sys.stdin.readline

N=int(input())
S=[list(map(int,input().split())) for _ in range(N)]

players=[i for i in range(N)]

def team_score(team):
    score = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            score += S[team[i]][team[j]] + S[team[j]][team[i]]
    return score

answer=math.inf
for picked in combinations(players,N//2):
    team_start=list(picked)
    team_link=list(set(players)-set(team_start))
    
    score_start=team_score(team_start)
    score_link=team_score(team_link)
    answer=min(answer,abs(score_start-score_link))
print(answer)