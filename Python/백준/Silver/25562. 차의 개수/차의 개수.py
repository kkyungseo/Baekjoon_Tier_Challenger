import sys

N = int(sys.stdin.readline())

# 첫 번째 출력 (거리 합)
print(N * (N - 1) // 2)

# 첫 번째 출력 번호 패턴
number = 1
for _ in range(N):
    print(number, end=' ')
    number *= 2
print()

# 두 번째 출력 (N-1)
print(N - 1)

# 두 번째 출력 번호 패턴
number = 1
for _ in range(N):
    print(number, end=' ')
    number += 1
