import sys

# n : 입력받는 정수
n = int(input())

# n을 8로 나눈 나머지를 구한다 (1~8 사이의 반복 패턴을 위해)
n = n % 8

# n이 6, 7, 8(=0)인 경우에는 대칭되는 값으로 변환
# 예: 6 -> 2, 7 -> 1, 0 -> 0
if n > 5 or n == 0:
    result = (10 - n) % 8
else:
    result = n

# 결과 출력
print(result)