import sys

# N : 테스트케이스의 개수
N = int(input())

for i in range(N):
    # A, B : 두 개의 정수
    A, B = map(int, input().split())
    print(A + B)