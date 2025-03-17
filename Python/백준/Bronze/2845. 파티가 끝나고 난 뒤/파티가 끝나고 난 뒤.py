import sys

# L : 1제곱미터당 사람의 수
# P : 파티가 열렸던 곳의 넓이
L, P = map(int, input().split())

# num : 각 기사에 실려있는 참가자의 수 (양의 정수 5개)
num = list(map(int, input().split()))

if len(num) == 5:
    result = [n - (L * P) for n in num]
    print(*result, end=' ')
else:
    print(" ")