idx2sale_rate={0:10,1:20,2:30,3:40}

def solution(users, emoticons):
    
    N=len(users)
    M=len(emoticons)
    
    def check(idxs):
        ret=[0,0]
        for u_rate,u_price in users:
            pay=0
            is_register=False
            for i,idx in enumerate(idxs):
                if idx2sale_rate[int(idx)]>=u_rate:
                    pay+=emoticons[i]*(100-idx2sale_rate[int(idx)])//100
            if pay>=u_price:
                pay=0
                is_register=True
            if is_register:
                ret[0]+=1
            ret[1]+=pay
        return ret
                
    result=[]
    def P(idxs): # idxs is string
        # base-condition
        if len(idxs)==M:
            result.append(check(idxs))
            return
        for idx in range(4):
            P(idxs+str(idx))
            
    P("")
    result.sort(reverse=True)
    
    answer = result[0]
    return answer

