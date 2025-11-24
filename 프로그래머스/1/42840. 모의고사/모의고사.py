def solution(answers):
    p1=[1,2,3,4,5]
    p2=[2,1,2,3,2,4,2,5]
    p3=[3,3,1,1,2,2,4,4,5,5]
    N=len(answers)
    result=[0]*3
    for i in range(N):
        cur_answer=answers[i]
        cur_p1=p1[i%len(p1)]
        cur_p2=p2[i%len(p2)]
        cur_p3=p3[i%len(p3)]
        if cur_answer==cur_p1:
            result[0]+=1
        if cur_answer==cur_p2:
            result[1]+=1
        if cur_answer==cur_p3:
            result[2]+=1
    
    max_score=max(result)
    answer=[index+1 for index, score in enumerate(result) if score==max_score] 
    return answer