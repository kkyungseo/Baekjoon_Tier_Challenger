import sys

# A, B : 두 개의 정수

A, B = map(int, input().split())

result = (A + B) * (A - B)

print(result)