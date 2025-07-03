import sys
input=sys.stdin.readline

N=int(input())
numbers=sorted(list(map(int,input().split())))
count=0
for target_index in range(len(numbers)):
    # two pointers
    # [left, right)
    target=numbers[target_index]
    left,right=0,N
    
    while left<right-1:
        if left==target_index:
            left+=1
            continue
        if right-1==target_index:
            right-=1
            continue
        curr_sum=numbers[left]+numbers[right-1]
        if curr_sum<target:
            left+=1
        elif curr_sum>target:
            right-=1
        else:
            #print(target," is good!")
            count+=1

            break

print(count)
