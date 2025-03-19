import sys

# N, M : 입력받는 두 개의 정수
N, M = map(int, input().split())

for _ in range(N) :
    row = input().strip()
    print(row[::-1])