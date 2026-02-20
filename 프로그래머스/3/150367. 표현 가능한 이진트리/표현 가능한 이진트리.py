def solution(numbers):
    
    def is_valid(tree):
        ''' Return 1 in success'''
        def P(l,r)->bool:
            ''' Return True if tree[l,r) is valid'''
            # base-condition
            if l>=r:
                return True
            mid=(l+r-1)//2
            if tree[mid]=="0":
                if "1" in tree[l:r]:
                    return False
                return True
            return P(l,mid) and P(mid+1,r)
        if P(0,len(tree)):
            return 1
        return 0
    
    answer=[]
    for number in numbers:
        b=bin(number)[2:]
        size=1
        while size<len(b):
            size=size*2+1
            b=b.zfill(size)
        result=is_valid(b)
        answer.append(result)
    
    
    return answer