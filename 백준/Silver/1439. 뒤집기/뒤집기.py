import sys
input=sys.stdin.readline

S=input()
prev=S[0]
changed_point=0
for s in S[1:]:
    if s!=prev:
        changed_point+=1
        prev=s

print(changed_point//2)