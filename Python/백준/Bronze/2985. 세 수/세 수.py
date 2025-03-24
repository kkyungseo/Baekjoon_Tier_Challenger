import sys

# 입력 받기
a, b, c = map(int, input().split())

# 사칙연산을 하나씩 시도하면서 맞는 등식을 찾기
if a + b == c:
    print(f"{a}+{b}={c}")
elif a - b == c:
    print(f"{a}-{b}={c}")
elif a * b == c:
    print(f"{a}*{b}={c}")
elif a / b == c:
    print(f"{a}/{b}={c}")
elif a == b + c:
    print(f"{a}={b}+{c}")
elif a == b - c:
    print(f"{a}={b}-{c}")
elif a == b * c:
    print(f"{a}={b}*{c}")
elif a == b / c:
    print(f"{a}={b}/{c}")