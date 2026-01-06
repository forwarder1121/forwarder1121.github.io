import sys
input=sys.stdin.readline

while True:
    
    CASE_INPUT=list(input().split())
    k,S=int(CASE_INPUT[0]),CASE_INPUT[1:]

    if k==0:
        break
    def P(state,idx):
        # base-condition
        if idx==k:
            if len(state)==6:
                print(*state)
            return 
        state.append(S[idx])
        P(state,idx+1)
        state.pop()
        P(state,idx+1)

        return 

    P([],0)
    print()