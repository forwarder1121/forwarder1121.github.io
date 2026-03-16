from collections import defaultdict,Counter
def solution(genres, plays):
    N=len(genres)
    counter=Counter()
    for i in range(N):
        counter[genres[i]]+=plays[i]
    
    answer=[]
    for genre,_ in counter.most_common():
        genre_list=[]
        for i in range(N):
            if genres[i]==genre:
                genre_list.append((i,plays[i]))
        genre_list.sort(key=lambda x:-x[1])
        cnt=0
        for idx,val in genre_list:
            if cnt==2:
                break
            answer.append(idx)
            cnt+=1
        
    
    return answer