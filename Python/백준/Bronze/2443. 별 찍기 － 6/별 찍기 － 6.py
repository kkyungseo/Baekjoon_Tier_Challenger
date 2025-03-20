import sys

input = sys.stdin.readline

# N : 입력받는 정수
N = int(input())

# 1번째 줄에 ( 2 * N - 1 ) 개의 별 출력

for i in range(1, N+1) :
    spaces = ' ' * (i - 1)
    stars = '*' * (2 * (N - i) + 1)
    print(spaces + stars)