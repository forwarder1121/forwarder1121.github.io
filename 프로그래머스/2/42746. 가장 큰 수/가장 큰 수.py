from functools import cmp_to_key
def solution(numbers):
    num=list(map(str,numbers))
    def compare(a,b):
        if a+b>b+a:
            return -1
        elif a+b<b+a:
            return 1
        else:
            return 0
    num.sort(key=cmp_to_key(compare))
    answer="".join(num)
    
    if answer[0]=="0":
        return "0"
    
    return answer