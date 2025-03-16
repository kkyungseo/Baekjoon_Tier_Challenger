import sys

# A, B : 입력받는 두 정수
A = int(input().strip())
B = int(input().strip())

# 두 정수의 합의 자릿수를 출력
print(len(str(A + B)))