import sys
input=sys.stdin.read

data=input().split()
N=int(data[0])
numbers=data[1:]

reversed_numbers=[int(num[::-1]) for num in numbers]
reversed_numbers.sort()

print(*reversed_numbers)