def solution(answers):
    p1=[1,2,3,4,5]
    p2=[2,1,2,3,2,4,2,5]
    p3=[3,3,1,1,2,2,4,4,5,5]
    scores=[0]*3
    for index in range(len(answers)):
        if p1[index%len(p1)]==answers[index]:
            scores[0]+=1
        if p2[index%len(p2)]==answers[index]:
            scores[1]+=1
        if p3[index%len(p3)]==answers[index]:
            scores[2]+=1
    max_score=max(scores)
    result = [index+1 for index,value in enumerate(scores) if value==max_score]
    return result