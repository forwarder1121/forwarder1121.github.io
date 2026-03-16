import math
def solution(N, K):
    
    def to_base_k(N,K):
        digits=""
        while N>0:
            digits+=str(N%K)
            N//=K
        ret=""
        for i in range(len(digits)-1,-1,-1):
            ret+=digits[i]
        return ret
    
    def is_prime(number):
        if number==1:
            return False
        for i in range(2,int(math.sqrt(number))+1):
            if number%i==0:
                return False
        return True
    
    N_base_k = to_base_k(N,K)
    print(N_base_k)
    answer=0
    # check N_base_k[start,end)
    for start in range(len(N_base_k)):
        for end in range(start+1,len(N_base_k)+1):
            substring=N_base_k[start:end]
            if "0" in substring:
                continue
            if is_prime(int(substring)):
                if start-1>=0 and N_base_k[start-1]!="0":
                    continue
                elif end<len(N_base_k) and N_base_k[end]!="0":
                    continue
                print("substring : ",substring)    
                answer+=1
    return answer

