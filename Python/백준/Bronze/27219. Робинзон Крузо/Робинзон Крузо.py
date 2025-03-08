import sys

# N : 주어진 날 수
N = int(input())

result = 'V' * (N // 5) + 'I' * (N % 5)

print(result)