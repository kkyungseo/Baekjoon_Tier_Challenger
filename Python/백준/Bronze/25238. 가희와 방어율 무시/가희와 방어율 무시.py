import sys

# A, B : 입력받는 두 정수
A, B = map(int, input().split())

result = (A - A * 0.01 * B)

if result >= 100:
    print(0)
else:
    print(1)
