def solution(s):
    
    alpha2num={
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
    
    print(alpha2num.keys())
    tmp=""
    answer = ""
    for ch in s:
        if ch.isdigit():
            answer+=ch
        else:
            tmp+=ch
            if tmp in alpha2num.keys(): 
                answer+=alpha2num[tmp]
                tmp=""
    
    return int(answer)