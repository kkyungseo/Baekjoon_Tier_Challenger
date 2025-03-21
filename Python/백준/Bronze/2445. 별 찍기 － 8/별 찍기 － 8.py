import sys

input = sys.stdin.readline

# N : 입력받는 정수
N = int(input())

for i in range(1,N+1):
    print(('*'*i + ' '*(N-i)) + (' ' * (N-i) + '*'*i))
    
for i in range(N-1,0,-1):
    print(('*'*i + ' ' * (N-i)) + (' ' * (N-i) + '*'*i))