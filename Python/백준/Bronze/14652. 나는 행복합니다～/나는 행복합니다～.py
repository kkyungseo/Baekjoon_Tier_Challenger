import sys

# 관중석의 왼쪽 위는 (0, 0), 오른쪽 아래는 (N-1, M-1)으로 표시

# N, M : 관중석 크기
# K : 잃어버린 관중석 번호
N, M, K = map(int, input().split())

n = K // M
m = K % M

print(n, m)