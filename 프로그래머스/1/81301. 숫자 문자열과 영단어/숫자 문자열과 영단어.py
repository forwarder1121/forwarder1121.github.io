voc2num={
    "zero":"0",
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9",
}
def solution(S):
    result=""
    idx=0
    while idx<len(S):
        if S[idx].isdigit():
            result+=S[idx]
            idx+=1
        else: # 문자일 경우 숫자로 변환
            voc=""
            while voc not in voc2num:
                voc+=S[idx]
                idx+=1
            # voc에는 현재 완성된 문자열이 있음 ex) "seven"
            result+=voc2num[voc]
    
    return int(result)