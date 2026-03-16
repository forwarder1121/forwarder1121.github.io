import sys,math
input=sys.stdin.readline

A,B=map(int,input().split())

print(math.gcd(A,B))
print(A*B//math.gcd(A,B))