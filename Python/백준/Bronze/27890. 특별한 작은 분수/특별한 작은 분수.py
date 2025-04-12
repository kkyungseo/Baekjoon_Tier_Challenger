import sys

# 입력
x, n = map(int, input().split())

# N초 동안 시뮬레이션 (비트연산자 특성 이용)
for _ in range(n):
    if x % 2 == 0:
        x = (x // 2) ^ 6
    else:
        x = (2 * x) ^ 6

# 출력
print(x)