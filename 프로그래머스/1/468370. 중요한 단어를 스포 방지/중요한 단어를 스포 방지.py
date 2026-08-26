def solution(message, spoiler_ranges):
    # message의 항상 하나의 공백으로 시작하고 끝난다.
    if not message[0]==" ":
        message=" "+message
        new_spoiler_ranges=[]
        for s,e in spoiler_ranges:
            new_spoiler_ranges.append((s+1,e+1))
        spoiler_ranges=new_spoiler_ranges
    if not message[-1]==" ":
        message+=" " 
        
    N=len(message)
    M=len(spoiler_ranges)
    
    nonspoiler_words=set() # 스포일러가 아닌 단어
    spoiler_words=set() # 스포일러 단어
    
    # nonspoiler_words 초기화 O(NM)
    # message[idx]를 검사한다.
    idx=0
    cur_word=""
    while idx<N:
        character=message[idx]
        if character==" ":
            if cur_word:
                nonspoiler_words.add(cur_word)
                cur_word=""
            idx+=1
        else:
            is_spoiler_idx=False
            for s,e in spoiler_ranges:
                if s<=idx<=e:
                    is_spoiler_idx=True
                    cur_word=""
                    while message[idx]!=" ":
                        idx+=1
                    break
            if not is_spoiler_idx:
                cur_word+=character
                idx+=1

    
    # 스포 구간 마다
    # 만일 모든 문자가 공개 되었다면, W라 하자.
    # W가 nonspoiler_words에 없다면
    # spoiler_words에 W를 추가
    
    for s,e in spoiler_ranges:
        
        # 구간 [s,e]가 공개되었다.
        # 단어의 시작과 끝인 (ws,we)로 확장시킨다.
        # 이때 ws,we는 항상 공백을 가르킨다.
        ws,we=s,e
        while message[ws]!=" ":
            ws-=1
        while message[we]!=" ":
            we+=1
        cur_word="" # 현재 공개된 단어
        idx=ws+1
        while idx<=we:
            character=message[idx]
            if character==" ":
                # cur_word는 완전히 공개된 단어이다.
                if cur_word:
                    if cur_word not in nonspoiler_words:
                        spoiler_words.add(cur_word)
                    cur_word=""
                idx+=1
                
            else:
                cur_word+=character
                idx+=1
            
    return len(spoiler_words)
  