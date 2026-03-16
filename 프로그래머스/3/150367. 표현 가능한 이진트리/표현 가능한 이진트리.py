def solution(numbers):
    
    def is_valid(tree):
        ''' Returns 1 on success, 0 in failure'''
        def P(l,r):
            ''' Return bool according by number[l:r) is valid'''
            # base-condition
            if l>=r:
                return True
            mid=(l+r-1)//2
            
            left_valid=P(l,mid)
            right_valid=P(mid+1,r)
            
            if not left_valid or not right_valid:
                return False
            if tree[mid]=="0":
                if "1" in tree[l:r]:
                    return False
            return True
        if P(0,len(tree)):
            return 1
        else:
            return 0
            
            
        
            
    
    answer = []
    for number in numbers:
        b=bin(number)[2:]
        size=1
        while size<len(b):
            size=size*2+1
        b=b.zfill(size)
        result=is_valid(b)
        answer.append(result)
        
    
    return answer