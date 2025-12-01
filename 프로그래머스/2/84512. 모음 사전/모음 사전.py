def solution(word):
    
    vowels=["A","E","I","O","U"]
    dictionary=[]
    
    def dfs(state):
        # base-condition
        if len(state)>5:
            return
        # apply
        dictionary.append(state)
        # dfs
        for v in vowels:
            dfs(state+v)
    
    dfs("")
    
    return dictionary.index(word)
    